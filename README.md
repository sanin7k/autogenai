# 🤖 AutogenAI

**Unified, pluggable SDK for LLMs — OpenAI, Gemini, and more.**  
Production-grade interface for integrating and abstracting multiple LLM providers via a clean Python API.

---

## 🚀 Features

- ✅ Easy-to-use `chat()` interface for multiple LLMs
- ✅ Supports **OpenAI** and **Gemini** out of the box
- ✅ Built-in error handling (`LLMResponseError`)
- ✅ Easily extendable for other providers (Claude, Mistral, Ollama, etc.)
- ✅ Semantic versioning & PyPI-ready

---

## 📦 Installation

From PyPI (once released):

```bash
pip install autogenai
From TestPyPI (for testing pre-releases):

bash
Copy code
pip install -i https://test.pypi.org/simple/ autogenai
From GitHub (dev version):

bash
Copy code
pip install git+https://github.com/yourusername/autogenai.git
🧠 Quick Start
✅ OpenAI Example
python
Copy code
from autogenai import OpenAIEngine

engine = OpenAIEngine(api_key="your-openai-api-key")
response = engine.chat("Tell me a joke.")
print(response)
✅ Gemini Example
python
Copy code
from autogenai import GeminiEngine

engine = GeminiEngine(api_key="your-gemini-api-key")
response = engine.chat("What's the capital of Japan?")
print(response)
🧪 Advanced Usage
✅ Injecting custom config
python
Copy code
from autogenai import OpenAIEngine

engine = OpenAIEngine(
    api_key="your-openai-api-key",
    model="gpt-4",
    system_prompt="You are a helpful assistant.",
)
✅ Error Handling
python
Copy code
from autogenai.utils.errors import LLMResponseError

try:
    engine.chat("Hello!")
except LLMResponseError as e:
    print(f"Request failed: {e}")
    print("Status Code:", e.status_code)
    print("Response Data:", e.response_data)
🧩 Extending to Other LLMs
You can subclass BaseEngine to support any provider:

python
Copy code
from autogenai.core.base import BaseEngine

class MyLLMEngine(BaseEngine):
    def chat(self, prompt: str) -> str:
        # Implement your own logic here
        ...
🔧 Project Structure
bash
Copy code
autogenai/
├── core/           # LLM engines (OpenAI, Gemini)
├── utils/          # Error classes, config loading
├── examples/       # Usage demos
├── tests/          # Unit tests

📜 License
This project is licensed under the MIT License.

👨‍💻 Author
Built with ❤️ by Sanin K

🧭 Roadmap
 CLI support (autogenai chat "hi")

 Add Claude / Mistral / Ollama adapters

 Async support with httpx.AsyncClient

 Prompt templating

 Streaming & function calling support

📦 Changelog
See CHANGELOG.md for version history.

🐛 Contributing
Pull requests are welcome! Please open an issue first to discuss major changes.

⭐ Star if you like it!
If you find this useful, please star ⭐ the repo. It helps others discover it too!
