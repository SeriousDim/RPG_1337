from dataclasses import dataclass

from model.common.health import Health
from model.player.player_level import PlayerLevel
from model.player.statistics import Statistics
from prompt.model.item_dto import ItemDto
from prompt.model.player_armor_dto import PlayerArmorDto


@dataclass
class Player:
    level: PlayerLevel
    statistics_for_current_session: Statistics
    health: Health
    money: int
    inventory: list[ItemDto]
    armor: PlayerArmorDto
    
    def to_dict(self):
        return {
            "level": self.level.to_dict(),
            "statistics_for_current_session": self.statistics_for_current_session.to_dict(),
            "health": self.health.to_dict(),
            # "money": self.money, # деньги пока не используются
            "inventory": [item.to_dict() for item in self.inventory],
            "armor": self.armor.to_dict()
        }

