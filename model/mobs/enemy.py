from dataclasses import dataclass

from model.common.health import Health


@dataclass
class Enemy:
    name: str
    rank: int
    health: Health
    damage_per_turn: int
    money_for_killing_this_enemy: int
