from dataclasses import dataclass

from model.items.item import Item

@dataclass
class Armor(Item):
    absorbed_damage: int
