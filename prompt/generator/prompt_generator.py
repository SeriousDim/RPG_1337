from langchain_core.prompts import ChatPromptTemplate

from core.resource_loader import ResourceLoader


def create_prompt(prompt_name: str):
    prompt_template = find_prompt_template_by_name(prompt_name)
    
    return ChatPromptTemplate.from_messages([
        ("human", prompt_template)
    ])


def find_prompt_template_by_name(prompt_name: str):
    return ResourceLoader.load_text(f"prompts/{prompt_name}.txt")
