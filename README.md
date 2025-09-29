# BasicChatbot

This repository contains a basic chatbot implementation using Python. The project demonstrates the integration of AI-driven conversational models and provides examples of how to use them effectively.

## Project Structure

```
BasicChatbot/
├── OpenRouter.py   # Streamlit-based chatbot using OpenRouter API
├── practice.py     # Example script for Google GenAI (Gemini) integration
├── practice2.py    # Additional example script for Google GenAI (Gemini)
```

## Prerequisites

1. **Python**: Ensure Python 3.7 or higher is installed.
2. **Dependencies**: Install the required Python libraries using the command below:
   ```bash
   pip install -r requirements.txt
   ```
3. **Environment Variables**: Create a `.env` file in the root directory with the following keys:
   ```
   GOOGLE_API_KEY=<your_google_api_key>
   OPENROUTER_API_KEY=<your_openrouter_api_key>
   ```

## Usage

### 1. Google GenAI (Gemini) Examples

- **`practice.py`**: Demonstrates how to use Google GenAI to generate content. Run the script:
  ```bash
  python practice.py
  ```

- **`practice2.py`**: Another example with a specific configuration for Google GenAI. Run the script:
  ```bash
  python practice2.py
  ```

### 2. OpenRouter Chatbot

- **`OpenRouter.py`**: A Streamlit-based chatbot interface using the OpenRouter API. To run the chatbot:
  ```bash
  streamlit run OpenRouter.py
  ```

  Open the provided URL in your browser to interact with the chatbot.

## Features

- **Google GenAI (Gemini)**:
  - Generate AI-driven content using the `gemini-2.5-flash` model.
  - Securely manage API keys using environment variables.

- **OpenRouter Chatbot**:
  - Build a chatbot interface using Streamlit.
  - Integrate OpenRouter API for conversational AI.

## Environment Variables

The project uses the `dotenv` library to load environment variables from a `.env` file. Ensure the following keys are set:

- `GOOGLE_API_KEY`: API key for Google GenAI.
- `OPENROUTER_API_KEY`: API key for OpenRouter.

## Dependencies

Add the following dependencies to your `requirements.txt` file:

```
google-genai
openai
streamlit
python-dotenv
```

Install them using:
```bash
pip install -r requirements.txt
```

## Notes

- Ensure your `.env` file is not included in version control for security purposes. This is already handled by the `.gitignore` file.
- The project is structured to be modular and easy to extend for additional AI models or APIs.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [Google GenAI (Gemini)](https://cloud.google.com/genai)
- [OpenRouter](https://openrouter.ai)
- [Streamlit](https://streamlit.io)