from dataclasses import dataclass, field
from enum import Enum

from model.items.item import Item


@dataclass
class ResourceType(Enum):
    HERB = "трава"
    ORE = "руда"


@dataclass
class Resource(Item):
    type: str = field(init=False)
    name: str
    resource_type: ResourceType
    min_instrument_rank: int
    
    def __post_init__(self):
        self.type = self.resource_type.value
    
    def __dict__(self):
        return {
            "name": self.name,
            "type": self.type,
            "rank": self.rank,
            "min_instrument_rank": self.min_instrument_rank
        }
    
