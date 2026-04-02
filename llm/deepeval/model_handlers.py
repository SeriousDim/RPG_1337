from deepeval.models import DeepEvalBaseLLM, GPTModel, AnthropicModel, OpenRouterModel

from llm.deepeval.gemini import GeminiViaHttpLLM
from llm.llm_keys import GPT_5_2
from llm.providers import Provider


def create_gpt_model(model_name: str, provider: Provider):
    result = GPTModel(
        model=model_name,
        api_key=provider.api_key,
        base_url="{provider.base_url}/openai/v1",
    )
    
    if model_name == GPT_5_2:
        result.model_data.supports_log_probs = True
    
    return result


def create_anthropic_model(model_name: str, provider: Provider):
    return AnthropicModel(
        model=model_name,
        api_key=provider.api_key,
        base_url="{provider.base_url}/anthropic",
    )


def create_gemini_model(model_name: str, provider: Provider):
    return GeminiViaHttpLLM(
        model=model_name,
        api_key=provider.api_key,
        base_url="{provider.base_url}/google",
    )


def create_open_router_model(model_name: str, provider: Provider):
    return OpenRouterModel(
        model=model_name,
        api_key=provider.api_key,
        base_url="{provider.base_url}/openrouter/v1",
    )
