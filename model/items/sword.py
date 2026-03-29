from dataclasses import dataclass

from model.items.weapon import Weapon

from dataclasses import dataclass, field

from model.items.weapon import Weapon


@dataclass
class Sword(Weapon):
    type: str = field(init=False)
    damage_per_enemy: int
    enemies_to_hit: int
