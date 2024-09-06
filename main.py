import json
import os
import logging
from dotenv import load_dotenv
from agents import IndustryStrategist, ExpertAuthor, CriticalReviewer, FinalEditor
from document_utils import save_outline, parse_outline, compile_document, save_document
from api_handlers import CLAUDE_MODEL, GPT_MODEL

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
load_dotenv()

def load_json_config(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"Configuration file '{filename}' not found.")
        raise
    except json.JSONDecodeError:
        logging.error(f"Error parsing configuration file '{filename}'. Please ensure it's valid JSON.")
        raise

def main():
    try:
        # Load configuration
        config = load_json_config('config.json')
        logging.info("Configuration loaded successfully")
        logging.info(f"Using GPT model: {GPT_MODEL}")
        logging.info(f"Using Claude model: {CLAUDE_MODEL}")
        
        # Generate outline
        logging.info("Generating outline...")
        outline = IndustryStrategist.generate_outline(config['document'], config['api_config']['openai']['max_tokens'])
        save_outline(outline, 'outline.md')
        logging.info("Outline saved to outline.md")
        
        # Parse outline
        sections = parse_outline('outline.md')
        logging.info(f"Parsed {len(sections)} sections from outline")
        
        if not sections:
            logging.warning("No sections found in outline. Stopping process.")
            return
        
        # Generate and enhance content
        final_content = []
        for i, section in enumerate(sections, 1):
            logging.info(f"Processing section {i}/{len(sections)}: {section}")
            
            logging.info("Generating initial content...")
            initial_content = ExpertAuthor.generate_content(section, config, config['api_config']['openai']['max_tokens'])
            
            logging.info("Reviewing content...")
            feedback = CriticalReviewer.review_content(initial_content, section, config, config['api_config']['openai']['max_tokens'])
            
            logging.info("Enhancing content...")
            try:
                enhanced_content = FinalEditor.enhance_content(initial_content, feedback, config, config['api_config']['anthropic']['max_tokens'])
            except Exception as e:
                logging.error(f"Failed to enhance content: {str(e)}")
                enhanced_content = initial_content  # Fall back to unenhanced content
            
            final_content.append(enhanced_content)
        
        # Compile and save document
        logging.info("Compiling final document...")
        document = compile_document(config['document']['title'], final_content)
        save_document(document, config['output']['filename'])
        logging.info(f"Document saved as {config['output']['filename']}")
        
        # Log final document statistics
        with open(config['output']['filename'], 'r') as f:
            final_doc = f.read()
        logging.info(f"Final document length: {len(final_doc)} characters")
        logging.info(f"Final document word count: {len(final_doc.split())}")

    except Exception as e:
        logging.error(f"An error occurred during document generation: {e}")
        raise

if __name__ == "__main__":
    main()