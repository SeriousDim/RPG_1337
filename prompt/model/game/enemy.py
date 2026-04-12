from dataclasses import dataclass

from model.common.health import Health
from model.objects.get_rank import get_max_enemy_rank
from prompt.model.rank_dto import RankDto


@dataclass
class Enemy:
    name: str
    rank: RankDto
    health: Health
    damage_per_turn: int
    money_for_killing_this_enemy: int
    
    def __init__(self, enemy):
        self.name = enemy.name
        self.rank = RankDto(enemy.rank, get_max_enemy_rank())
        self.health = enemy.health
        self.damage_per_turn = enemy.damage_per_turn
        self.money_for_killing_this_enemy = enemy.money_for_killing_this_enemy
    
    def to_dict(self):
        return {
            "name": self.name,
            "rank": self.rank.to_dict(),
            "health": self.health.to_dict(),
            "damage_per_turn": self.damage_per_turn,
            # "money_for_killing_this_enemy": self.money_for_killing_this_enemy # деньги пока не используются
        }