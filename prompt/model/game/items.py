from dataclasses import dataclass

from prompt.model.item_dto import ItemDto
from prompt.model.game.armors import Armors
from prompt.model.game.resources import Resources
from model.game.context.items import Items as ModelItems


@dataclass
class Items:
    resources: Resources
    weapons: list[ItemDto]
    instruments: list[ItemDto]
    armor: Armors
    
    def __init__(self, items: ModelItems):
        self.resources = Resources(items.resources)
        self.weapons = [ItemDto(weapon) for weapon in items.weapons]
        self.instruments = [ItemDto(instrument) for instrument in items.instruments]
        self.armor = Armors(items.armor)
    
    def __dict__(self):
        return {
            "resources": self.resources.__dict__(),
            "weapons": [weapon.__dict__() for weapon in self.weapons],
            "instruments": [instrument.__dict__() for instrument in self.instruments],
            "armor": self.armor.__dict__()
        }