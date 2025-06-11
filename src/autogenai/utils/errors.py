class LLMEngineError(Exception):
    """Base exception for all LLM engine issues."""

class InvalidEngineError(LLMEngineError):
    """Raised when an unsupported engine is requested."""

class MissingAPIKeyError(LLMEngineError):
    """Raised when a required API key is missing from the .env file."""
