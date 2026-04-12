from dataclasses import dataclass

from prompt.model.item_dto import ItemDto


@dataclass
class Resources:
    herbs: list[ItemDto]
    ores: list[ItemDto]
    
    def __init__(self, resources):
        self.herbs = [ItemDto(herb, exclude_fields=['resource_type']) for herb in resources.herbs]
        self.ores = [ItemDto(ore, exclude_fields=['resource_type']) for ore in resources.ores]
    
    def to_dict(self):
        return {
            "herbs": [herb.to_dict() for herb in self.herbs],
            "ores": [ore.to_dict() for ore in self.ores]
        }