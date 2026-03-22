from dataclasses import dataclass

from model.items.weapon import Weapon

@dataclass
class Sword(Weapon):
    damage_per_enemy: int
    enemies_to_hit: int
