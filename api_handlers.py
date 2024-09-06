import os
import json
import logging
import time
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_random_exponential
import openai
from anthropic import Anthropic, APIConnectionError, RateLimitError, APIStatusError

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load configuration
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Constants from config
CLAUDE_MODEL = config['api_config']['anthropic']['model']
GPT_MODEL = config['api_config']['openai']['model']
DELAY_BETWEEN_CALLS = config['api_config']['delay_between_calls']

# Initialize API clients
openai_client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
anthropic_client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(5))
def call_gpt4(prompt, max_tokens=None):
    if max_tokens is None:
        max_tokens = config['api_config']['openai']['max_tokens']
    try:
        response = openai_client.chat.completions.create(
            model=GPT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens
        )
        logging.info(f"GPT-4 API call: Input tokens: {response.usage.prompt_tokens}, Output tokens: {response.usage.completion_tokens}")
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"Error calling GPT-4 API: {e}")
        raise

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(5))
def call_claude(prompt, max_tokens=None):
    if max_tokens is None:
        max_tokens = config['api_config']['anthropic']['max_tokens']
    try:
        response = anthropic_client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=max_tokens,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        logging.info(f"Claude API call: Input tokens: {response.usage.input_tokens}, Output tokens: {response.usage.output_tokens}")
        return response.content[0].text
    except APIConnectionError as e:
        logging.error(f"The server could not be reached: {e.__cause__}")
        raise
    except RateLimitError as e:
        logging.error(f"Rate limit exceeded: {e}")
        raise
    except APIStatusError as e:
        logging.error(f"API error: Status {e.status_code}, Response: {e.response}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error in Claude API call: {str(e)}")
        raise

def delay_between_calls():
    time.sleep(DELAY_BETWEEN_CALLS)

if __name__ == "__main__":
    # You can add some simple tests here to verify the functions work correctly
    test_prompt = "Explain the concept of artificial intelligence in one sentence."
    
    print("Testing GPT-4 API call:")
    gpt4_response = call_gpt4(test_prompt)
    print(gpt4_response)
    
    delay_between_calls()
    
    print("\nTesting Claude API call:")
    claude_response = call_claude(test_prompt)
    print(claude_response)