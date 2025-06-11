import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

models = genai.list_models()
for m in models:
    print(m.name, "→", m.supported_generation_methods)