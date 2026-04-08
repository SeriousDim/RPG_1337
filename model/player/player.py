from dataclasses import dataclass

from model.items.item import Item
from model.common.health import Health
from model.player.player_armor import PlayerArmor
from model.player.player_level import PlayerLevel
from model.player.statistics import Statistics


@dataclass
class Player:
    level: PlayerLevel
    statistics_for_current_session: Statistics
    health: Health
    money: int
    inventory: list[Item]
    armor: PlayerArmor
