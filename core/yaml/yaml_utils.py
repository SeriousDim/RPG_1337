from dataclasses import asdict, fields, is_dataclass
from enum import Enum
from functools import wraps
from typing import Any, Callable


def to_yaml_primitive(value: Any) -> Any:
    """Приводит значения к виду, который безопасно дампится в YAML."""
    if isinstance(value, Enum):
        return value.value  # или value.name — как вам нужно
    if is_dataclass(value):
        return {f.name: to_yaml_primitive(getattr(value, f.name)) for f in fields(value)}
    if isinstance(value, dict):
        return {k: to_yaml_primitive(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [to_yaml_primitive(v) for v in value]
    return value


def _surround_with_yaml_block(func: Callable[..., str]) -> Callable[..., str]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        result = func(*args, **kwargs)
        return f"```yaml\n{result}\n```"
    return wrapper
