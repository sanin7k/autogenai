import httpx
from autogenai.core.base import BaseLLM
from autogenai.utils.logger import get_logger
from autogenai.utils.config import get_env, DEFAULT_MODELS
from autogenai.utils.errors import MissingAPIKeyError

logger = get_logger("OpenAIEngine")

class OpenAIEngine(BaseLLM):
    def __init__(self, model: str = None):
        try:
            self.api_key = get_env("OPENAI_API_KEY", required=True)
        except EnvironmentError:
            raise MissingAPIKeyError("OPEN_API_KEY is required but not set.")
        self.model = model or DEFAULT_MODELS["openai"]
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
            raise None
        except httpx.RequestError as e:
            logger.error(f"Request failed: {e}")
            raise None

    def summarize(self, text: str) -> str:
        prompt = f"Summarize the following text:\n\n{text}"
        return self.chat(prompt)
