from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_openrouter import ChatOpenRouter

from llm.providers import Provider


def create_gpt_model(model_name: str, provider: Provider):
    return ChatOpenAI(
        model=model_name,
        api_key=provider.api_key,
        base_url=f"{provider.base_url}/openai/v1",
        logprobs=model_name == "gpt-5.2"
    )


def create_anthropic_model(model_name: str, provider: Provider):
    return ChatAnthropic(
        model=model_name,
        api_key=provider.api_key,
        base_url=f"{provider.base_url}/anthropic",
    )


def create_gemini_model(model_name: str, provider: Provider):
    return ChatGoogleGenerativeAI(
        model=model_name,
        google_api_key=provider.api_key,
        client_options={"api_endpoint": f"{provider.base_url}/google"},
    )


def create_open_router_model(model_name: str, provider: Provider):
    return ChatOpenRouter(
        model=model_name,
        api_key=provider.api_key,
        base_url=f"{provider.base_url}/openrouter/v1",
    )

