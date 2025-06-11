import os
import google.generativeai as genai
from dotenv import load_dotenv

from autogenai.core.base import BaseLLM
from autogenai.utils.logger import get_logger

load_dotenv()
logger = get_logger("GeminiEngine")

class GeminiEngine(BaseLLM):
    def __init__(self, api_key: str = None, model: str = "models/gemini-1.5-flash"):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("Gemini API key not provided")
        self.model = model
        genai.configure(api_key=self.api_key)
        self.chat_model = genai.GenerativeModel(model)
        logger.info(f"GeminiEngine initialized with model: {model}")

    def chat(self, prompt: str) -> str:
        try:
            logger.info("Sending Gemini chat request...")
            response = self.chat_model.generate_content(prompt)
            logger.info("Gemini response received.")
            return response.text.strip()
        except Exception as e:
            logger.error(f"Gemini chat error: {e}")
            raise

    def summarize(self, text: str) -> str:
        prompt = f"Summarize the following text:\n\n{text}"
        return self.chat(prompt)