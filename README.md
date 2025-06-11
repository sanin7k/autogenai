# 🔮 autogenai

⚠️ This is an early-stage SDK. Interfaces and behaviors may change in minor releases.

**Early-stage unified SDK for LLMs like OpenAI, Gemini and more. — Simple, Pluggable, and Ready for Production**

---

## ✨ Features

- 🧠 Unified interface for LLMs (OpenAI, Gemini, etc.)
- 🛠️ Automatically loads from `.env` (`OPENAI_API_KEY`, `GEMINI_API_KEY`, `LLM_ENGINE`, `DEFAULT_OPENAI_MODEL`, `DEFAULT_GEMINI_MODEL`)
- 🚨 Built-in error handling: `APIMissingError`, `LLMResponseError`
- 🧪 100% test coverage with `pytest`
- 🔧 CLI included for quick interaction
- 📦 PyPI-ready structure with semantic versioning

---

## 📦 Installation

```bash
pip install autogenai

```
Or, from source:
```bash
git clone https://github.com/sanin7k/autogenai-sdk.git
cd autogenai
pip install .
```

---

## ⚙️ Configuration

Create a .env file in your project root:
```env
# Required (one or both depending on engine used)
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_google_key

# Optional engine & model settings
LLM_ENGINE=openai  # or gemini
DEFAULT_OPENAI_MODEL=gpt-3.5-turbo
DEFAULT_GEMINI_MODEL=gemini-1.5-pro
```
If a required API key is missing, APIMissingError will be raised at runtime.

---

## 🚀 Usage (Python)
```python
from autogenai.core.factory import LLMFactory

engine = LLMFactory.create() # uses LLM_ENGINE from .env or defaults to Gemini
response = engine.chat("Tell me a joke")
print(response)

```

---

## 🧪 Testing

Run all tests:

```bash
pytest
```
Includes mocks for external calls and full coverage for OpenAIEngine, GeminiEngine, and factory.

---

## 💻 CLI Usage

You can also use the SDK via command line:
```bash
autogenai chat "What's the capital of France?"
```

Or for Gemini specifically:

```bash
autogenai chat "What's the capital of France?" --engine "gemini"
```

---

## 📂 Project Structure

```bash
autogenai-sdk/
├── examples/
│   ├── openai_chat.py
│   ├── sdk_chat.py
│   ├── sdk_cli.py
│   └── simple_chat.py
├── src/autogenai/
│   ├── core/
│   │   ├── base.py
│   │   ├── factory.py
│   │   ├── gemini_engine.py
│   │   └── openai_engine.py
│   ├── utils/
│   │   ├── config.py
│   │   ├── errors.py
│   │   └── logger.py
│   ├── cli.py
│   └── tools.py
├── tests/
│   ├── test_factory.py
│   └── test_openai.py
├── .env
├── README.md
├── requirements.txt
└── pyproject.toml

```

---

## 📖 Error Handling

**APIMissingError**

Raised when API key is not found in .env.
```python
raise MissingAPIKeyError("Missing OpenAI API key.")
```

**LLMResponseError**

Raised when the API responds with an error (like 429 or 401).
```python
raise LLMResponseError("API failed", status_code=429, response_data={...})

```

---

## 🔢 Semantic Versioning

This SDK follows SemVer:
- MAJOR – breaking changes
- MINOR – new features, backward-compatible
- PATCH – bug fixes

Current version: 0.1.0

---

## 🙌 Contributing

1. Fork this repo
2. Create your feature branch (git checkout -b feat/my-feature)
3. Commit changes (git commit -am 'add cool feature')
4. Push to branch (git push origin feat/my-feature)
5. Open a pull request 🚀

---

## 📝 License
MIT License © 2025 Sanin K