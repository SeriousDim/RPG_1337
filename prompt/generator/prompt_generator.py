from langchain_core.prompts import ChatPromptTemplate

from core.resource_loader import ResourceLoader


def create_prompt(prompt_name: str):
    prompt_template = find_prompt_template_by_name(prompt_name)
    
    return ChatPromptTemplate.from_messages([
        ("human", prompt_template)
    ])


def prompt_from_file(file_name: str):
    with open(file_name, "r") as file:
        return ChatPromptTemplate.from_messages([
            ("human", file.read())
        ])


def find_prompt_template_by_name(prompt_name: str):
    return ResourceLoader.load_text(f"prompts/{prompt_name}.txt")
