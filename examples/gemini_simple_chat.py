from autogenai.core.gemini_engine import GeminiEngine

engine = GeminiEngine()
response = engine.chat("Write a short inspirational message.")
print(response)