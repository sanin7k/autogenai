from autogenai.core.base import BaseLLM
import pytest

def test_base_methods_fail():
    class DummyLLM(BaseLLM):
        pass

    dummy = DummyLLM(api_key="fake")
    with pytest.raises(TypeError):
        dummy.chat("hello")
