# DocGen

## Multi-Agent AI Document Generator

A Python-based application that automates the creation of tailored documents using a multi-agent architecture integrated with AI models. This tool leverages OpenAI (GPT-4o) and Anthropic (Claude) APIs to deliver high-quality content, designed to meet diverse business documentation needs. It supports configurable workflows, flexible output formats, and robust error handling to ensure seamless document generation.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Customizing Document Generation](#customizing-document-generation)
  - [Output](#output)
- [Examples](#examples)
- [Error Handling and Logging](#error-handling-and-logging)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## Features

- **Multi-Agent Architecture**: Supports concurrent execution of multiple agents to handle various document generation tasks, improving efficiency and scalability.
- **API Integration**: Seamlessly integrates with OpenAI GPT-4o and Anthropic Claude models for state-of-the-art content generation.
- **Configurable Outputs**: Provides users with the ability to customize output formats, tones, and structures to suit different business requirements.
- **Dynamic Workflows**: Enables flexible agent workflows tailored to specific document generation needs, ensuring a versatile solution for diverse use cases.
- **Robust Error Handling**: Implements retry logic and error management to handle API call failures and connectivity issues.
- **Logging and Monitoring**: Detailed logging for monitoring application performance and debugging.

## Architecture

The application is built using a modular architecture:

- **`main.py`**: The main entry point that orchestrates the document generation process.
- **`agents.py`**: Contains definitions for various agents responsible for handling different parts of the document generation workflow.
- **`api_handlers.py`**: Manages interactions with external APIs (OpenAI and Anthropic), including sending requests and handling responses.
- **`document_utils.py`**: Provides utility functions for document formatting, saving, and other operations.
- **`config.json`**: A user-editable configuration file to specify document parameters, output preferences, and API settings.
- **`requirements.txt`**: Lists all dependencies required to run the application.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.7 or later
- API keys for OpenAI and Anthropic
- Access to a terminal or command line interface

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/terilios/DocGen.git
   cd DocGen
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:

   Create a `.env` file in the root directory of the project and add your API keys:

   ```bash
   OPENAI_API_KEY=your_openai_api_key
   ANTHROPIC_API_KEY=your_anthropic_api_key
   ```

### Configuration

Edit the `config.json` file to define your document requirements:

```json
{
  "document": {
    "title": "Your Document Title",
    "description": "A brief description of the content you need."
  },
  "output": {
    "format": "brief or detailed",
    "tone": "business or casual",
    "filename": "your_output_filename.md"
  },
  "api_config": {
    "delay_between_calls": 20,
    "openai": {
      "model": "gpt-4o",
      "max_tokens": 4000
    },
    "anthropic": {
      "model": "claude-3-5-sonnet-20240620",
      "max_tokens": 4000
    }
  }
}
```

## Usage

### Running the Application

To generate a document, run:

```bash
python main.py
```

### Customizing Document Generation

- **Title and Description**: Set the `title` and `description` in `config.json` to specify the topic and scope of your document.
- **Output Settings**: Adjust the `format` (e.g., "brief", "detailed") and `tone` (e.g., "business", "casual") to match the desired style.
- **API Configuration**: Modify the `api_config` section to change models, token limits, or delays between API calls.

### Output

Generated documents will be saved to the specified `filename` in `config.json`. The application supports various formats such as Markdown (`.md`), plain text (`.txt`), and more.

## Examples

1. **Generate a Brief Business Report**:

   Configure `config.json`:

   ```json
   {
     "document": {
       "title": "Market Trends Analysis",
       "description": "An overview of the latest trends in the AI market."
     },
     "output": {
       "format": "brief",
       "tone": "business",
       "filename": "market_trends_analysis.md"
     }
   }
   ```

   Run the application:

   ```bash
   python main.py
   ```

   Output: `market_trends_analysis.md` with a brief, business-oriented report.

2. **Generate a Detailed Casual Report**:

   Configure `config.json`:

   ```json
   {
     "document": {
       "title": "AI in Everyday Life",
       "description": "Exploring the impact of AI on daily activities."
     },
     "output": {
       "format": "detailed",
       "tone": "casual",
       "filename": "ai_everyday_life.txt"
     }
   }
   ```

   Run the application:

   ```bash
   python main.py
   ```

   Output: `ai_everyday_life.txt` with a detailed, casual report.

## Error Handling and Logging

- The application uses the `tenacity` library for retrying failed API calls due to network issues or rate limits.
- Logs are generated for each run and stored in the `logs/` directory, providing insights into the execution flow and error occurrences.

## Contributing

We welcome contributions to improve this project! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`feature/your-feature-name`).
3. Make your changes and commit them (`git commit -m "Add new feature"`).
4. Push the changes to your fork (`git push origin feature/your-feature-name`).
5. Open a pull request to the main branch.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions, suggestions, or feedback, please reach out to the project maintainer at [tdriscoll@terilios.com].

## Acknowledgments

- Special thanks to OpenAI for providing the GPT-4o model and Anthropic for the Claude model.
- Appreciation to all contributors and the open-source community for their support and feedback.
