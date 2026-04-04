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
    
    def __dict__(self):
        return {
            "helmets": [helmet.__dict__() for helmet in self.helmets],
            "chestplates": [chestplate.__dict__() for chestplate in self.chestplates],
            "leggings": [legging.__dict__() for legging in self.leggings],
            "shields": [shield.__dict__() for shield in self.shields]
        }