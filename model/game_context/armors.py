from dataclasses import dataclass

from model.items.armor import Armor


@dataclass
class Armors:
    helmets: list[Armor]
    chestplates: list[Armor]
    leggings: list[Armor]
    shields: list[Armor]
