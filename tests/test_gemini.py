import os
import pytest
from autogenai.core.gemini_engine import GeminiEngine

@pytest.mark.skipif(not os.getenv("GEMINI_API_KEY"), reason="No Gemini key")
def test_gemini_chat():
    engine = GeminiEngine()
    result = engine.chat("What is the capital of Italy?")
    assert "Rome" in result

@pytest.mark.skipif(not os.getenv("GEMINI_API_KEY"), reason="No Gemini key")
def test_gemini_summarize():
    engine = GeminiEngine()
    result = engine.summarize("The Colosseum is an ancient Roman arena in Rome.")
    assert "Colosseum" in result
