from dataclasses import dataclass

from model.items.resource import Resource


@dataclass
class Resources:
    herbs: list[Resource]
    ores: list[Resource]
