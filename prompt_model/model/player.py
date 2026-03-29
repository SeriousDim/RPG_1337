from dataclasses import dataclass

from model.player.health import Health
from model.player.player_level import PlayerLevel
from model.player.statistics import Statistics
from prompt_model.model.item_dto import ItemDto
from prompt_model.model.player_armor_dto import PlayerArmorDto


@dataclass
class Player:
    level: PlayerLevel
    statistics_for_current_session: Statistics
    health: Health
    money: int
    inventory: list[ItemDto]
    armor: PlayerArmorDto
