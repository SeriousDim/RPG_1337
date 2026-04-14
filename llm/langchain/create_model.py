from langchain_openai import ChatOpenAI

from llm.langchain.model_handlers import create_anthropic_model, create_open_router_model, create_gemini_model, create_gpt_model
from llm.providers import Provider

def create_langchain_model(key: str, provider: Provider):
    if provider.name == 'proxy_api':
        if key.startswith("gpt"):
            return create_gpt_model(key, provider)
        elif key.startswith("claude"):
            return create_anthropic_model(key, provider)
        elif key.startswith("gemini"):
            return create_gemini_model(key, provider)
        elif key.startswith("openrouter") or key.startswith("deepseek"):
            return create_open_router_model(key, provider)
        else:
            raise ValueError(f"Unknown model key: {key}")
    elif provider.name == 'router_ai':
        return ChatOpenAI(
            model=key,
            api_key=provider.api_key,
            base_url=f"{provider.base_url}"
        )
