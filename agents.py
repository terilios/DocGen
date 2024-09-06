import logging
from api_handlers import call_gpt4, call_claude, delay_between_calls

class IndustryStrategist:
    @classmethod
    def generate_outline(cls, document_info, max_tokens):
        prompt = f"""As an Industry Strategist with 30 years of experience, create a detailed outline for the following document:

Title: {document_info['title']}

Description: {document_info['description']}

Please provide the outline in markdown format, using '##' to denote main sections and '###' for subsections."""

        try:
            outline = call_gpt4(prompt, max_tokens)
            delay_between_calls()
            return outline
        except Exception as e:
            logging.error(f"Error generating outline: {e}")
            raise

class ExpertAuthor:
    @classmethod
    def generate_content(cls, section, config, max_tokens):
        prompt = f"""As an expert author with the following profile: {config['author']['profile']},
write initial content for the following section of a document:

Section: {section}

Document Title: {config['document']['title']}
Document Description: {config['document']['description']}

Please write in a {config['output']['tone']} tone and format the output as a {config['output']['format']}."""

        try:
            content = call_gpt4(prompt, max_tokens)
            delay_between_calls()
            return content
        except Exception as e:
            logging.error(f"Error generating content for section '{section}': {e}")
            raise

class CriticalReviewer:
    @classmethod
    def review_content(cls, content, section, config, max_tokens):
        prompt = f"""As a thorough and helpful critic, review the following content for the section "{section}" of the document titled "{config['document']['title']}".
Provide detailed feedback to enhance and improve the content, focusing on extending it with a critical eye and ensuring quality and thoroughness.

Content to review:
{content}

Please provide your feedback and suggestions for improvement."""

        try:
            feedback = call_gpt4(prompt, max_tokens)
            delay_between_calls()
            return feedback
        except Exception as e:
            logging.error(f"Error reviewing content for section '{section}': {e}")
            raise

class FinalEditor:
    @classmethod
    def enhance_content(cls, content, feedback, config, max_tokens):
        prompt = f"""As a final editor, please enhance the following content based on the provided feedback:

Initial Content:
{content}

Feedback:
{feedback}

Please maintain a {config['output']['tone']} tone and ensure the output remains in {config['output']['format']} format. 
Provide a comprehensive, enhanced version of the content."""

        try:
            enhanced_content = call_claude(prompt, max_tokens)
            delay_between_calls()
            return enhanced_content
        except Exception as e:
            logging.error(f"Error enhancing content: {e}")
            raise