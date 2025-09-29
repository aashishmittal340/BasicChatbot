
import os
from google import genai
from dotenv import load_dotenv  
from langchain.chat_models import init_chat_model


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
baseUrl = "https://genai.googleapis.com/v1beta2/models"
load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain the role of Baniya community in Indian economy.")
print(response.text)

