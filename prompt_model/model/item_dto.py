from dataclasses import dataclass, field, fields
from typing import Any

from engine.yaml_utils import _to_yaml_primitive
from model.items.item import Item
from model.objects import get_rank
from prompt_model.model.rank_dto import RankDto


@dataclass
class ItemDto(Item):
    rank: RankDto = field(init=False)
    extra: dict[str, Any] = field(default_factory=dict)
    
    def __init__(self, item: Item):
        all_data = {f.name: _to_yaml_primitive(getattr(item, f.name)) for f in fields(item)}

        self.name = all_data.pop("name")
        self.type = all_data.pop("type")

        rank = all_data.pop("rank")
        self.rank = RankDto(rank, get_rank(self.type))
        
        self.extra = all_data
