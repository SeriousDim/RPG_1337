from dataclasses import fields, is_dataclass
from enum import Enum
from typing import Any


def _to_yaml_primitive(value: Any) -> Any:
    """Приводит значения к виду, который безопасно дампится в YAML."""
    if isinstance(value, Enum):
        return value.value  # или value.name — как вам нужно
    if is_dataclass(value):
        return {f.name: _to_yaml_primitive(getattr(value, f.name)) for f in fields(value)}
    if isinstance(value, dict):
        return {k: _to_yaml_primitive(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_to_yaml_primitive(v) for v in value]
    return value
