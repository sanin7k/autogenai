import os
import pytest
from autogenai.core.openai_engine import OpenAIEngine

@pytest.mark.skipif(not os.getenv("OPENAI_API_KEY"), reason="No API key set")
def test_openai_chat():
    engine = OpenAIEngine()
    result = engine.chat("What is the capital of France?")
    assert "Paris" in result

@pytest.mark.skipif(not os.getenv("OPENAI_API_KEY"), reason="No API key set")
def test_openai_summarize():
    engine = OpenAIEngine()
    result = engine.summarize("The Eiffel Tower is in Paris. It is a tourist attraction.")
    assert "Eiffel Tower" in result
