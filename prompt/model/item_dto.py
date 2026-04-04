from dataclasses import dataclass, field, fields
from typing import Any

from core.yaml.yaml_utils import to_yaml_primitive
from model.items.item import Item
from model.objects.get_rank import get_max_rank
from prompt.model.rank_dto import RankDto


@dataclass
class ItemDto(Item):
    rank: RankDto = field(init=False)
    extra: dict[str, Any] = field(default_factory=dict)
    
    def __init__(self, item: Item, exclude_fields=[]):
        all_data = {f.name: to_yaml_primitive(getattr(item, f.name)) for f in fields(item)}

        for field in exclude_fields:
            del all_data[field]

        self.name = all_data.pop("name")
        self.type = all_data.pop("type")

        rank = all_data.pop("rank")
        self.rank = RankDto(rank, get_max_rank(self.type))
        
        self.extra = all_data
    
    def __dict__(self):
        return {
            "name": self.name,
            "type": self.type,
            "rank": self.rank.__dict__(),
            **self.extra
        }
