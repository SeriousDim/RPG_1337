from dataclasses import dataclass

from prompt.model.item_dto import ItemDto
from model.game.context.armors import Armors as ModelArmors


@dataclass
class Armors:
    helmets: list[ItemDto]
    chestplates: list[ItemDto]
    leggings: list[ItemDto]
    shields: list[ItemDto]
    
    def __init__(self, armors: ModelArmors):
        self.helmets = [ItemDto(helmet) for helmet in armors.helmets]
        self.chestplates = [ItemDto(chestplate) for chestplate in armors.chestplates]
        self.leggings = [ItemDto(legging) for legging in armors.leggings]
        self.shields = [ItemDto(shield) for shield in armors.shields]
    
    def to_dict(self):
        return {
            "helmets": [helmet.to_dict() for helmet in self.helmets],
            "chestplates": [chestplate.to_dict() for chestplate in self.chestplates],
            "leggings": [legging.to_dict() for legging in self.leggings],
            "shields": [shield.to_dict() for shield in self.shields]
        }