from google import genai
from google.genai import types
import os
from dotenv import load_dotenv      
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# baseUrl = "https://genai.googleapis.com/v1beta2/models" 

# The client gets the API key from the environment variable `GEMINI_API_KEY`.


client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Why Baniya community is important for Indian economy?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
    ),
)
print(response.text)