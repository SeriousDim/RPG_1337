from dataclasses import dataclass
from enum import Enum

from model.items.item import Item


@dataclass
class ResourceType(Enum):
    HERB = 1
    ORE = 2


@dataclass
class Resource(Item):
    name: str
    type: ResourceType
    min_instrument_rank: int
