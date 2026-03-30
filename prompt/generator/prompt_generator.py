from langchain_core.prompts import ChatPromptTemplate

from engine.resource_loader import ResourceLoader


def generate_prompt(prompt_name: str, context):
    prompt_template = find_prompt_template_by_name(prompt_name)
    filled_prompt = fill_context(prompt_template, context)
    
    return ChatPromptTemplate.from_messages([
        ("system", "Ты извлекаешь информацию и возвращаешь результат строго в указанном формате.")
    ])


def find_prompt_template_by_name(prompt_name: str):
    return ResourceLoader.load_text("prompts/{prompt_name}.txt")


def fill_context(template, context):
    return ""
