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
    
    def __dict__(self):
        return {
            "level": self.level.__dict__(),
            "statistics_for_current_session": self.statistics_for_current_session.__dict__(),
            "health": self.health.__dict__(),
            # "money": self.money, # деньги пока не используются
            "inventory": [item.__dict__() for item in self.inventory],
            "armor": self.armor.__dict__()
        }

