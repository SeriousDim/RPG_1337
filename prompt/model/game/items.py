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
    instrument_mapping: dict
    
    def __init__(self, items: ModelItems):
        self.resources = Resources(items.resources)
        self.weapons = [ItemDto(weapon) for weapon in items.weapons]
        self.instruments = [ItemDto(instrument) for instrument in items.instruments]
        self.armor = Armors(items.armor)
        self.instrument_mapping = items.instrument_mapping
    
    def to_dict(self):
        return {
            "resources": self.resources.to_dict(),
            "weapons": [weapon.to_dict() for weapon in self.weapons],
            "instruments": [instrument.to_dict() for instrument in self.instruments],
            "armor": self.armor.to_dict(),
            "instrument_mapping": self.instrument_mapping
        }
