import httpx
import os
from autogenai.core.base import BaseLLM
from autogenai.utils.logger import get_logger
from dotenv import load_dotenv

load_dotenv()
logger = get_logger("OpenAIEngine")

class OpenAIEngine(BaseLLM):
    def __init__(self, api_key: str = None, model: str = "gpt-3.5-turbo"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key not provided")
        self.model = model
        self.api_url = "https://api.openai.com/v1/chat/completions"
        self.client = httpx.Client(timeout=10)
        logger.info(f"OpenAIEngine initialized with model: {model}")

    def chat(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
        try:
            logger.info("Sending chat request...")
            response = self.client.post(self.api_url, headers=headers, json=data)
            response.raise_for_status()
            reply = response.json()["choices"][0]["message"]["content"]
            logger.info("Received response.")
            return reply.strip()
        except httpx.HTTPError as e:
            logger.error(f"OpenAI chat error: {e}\n")
            raise
        except httpx.RequestError as e:
            logger.error(f"Request failed: {e}")
            raise

    def summarize(self, text: str) -> str:
        prompt = f"Summarize the following text:\n\n{text}"
        return self.chat(prompt)
