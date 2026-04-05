from datetime import datetime

from langchain_core.messages import AIMessage

from prompt.parser.result import LlmResult


def replace_special_symbols(text: str) -> str:
    return text.replace("\\n", "\n")


def create_path_to_save(model_name: str) -> str:
    current_time = datetime.now().strftime("%d-%m-%y/%H-%M-%S")
    return f"{current_time}-{model_name}"


def parse_result(message: AIMessage) -> LlmResult:
    meta = message.model_dump()
    
    return LlmResult(
        content=replace_special_symbols(message.content),
        meta=meta,
        path_to_save=create_path_to_save(message.response_metadata['model_name'])
    )
