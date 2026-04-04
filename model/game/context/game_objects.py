from dataclasses import asdict, dataclass

from model.game.context.items import Items
from model.game.context.locations import Locations
from model.mobs.character import Character
from model.mobs.enemy import Enemy


@dataclass
class GameObjects:
    setting: str
    items: Items
    enemies: list[Enemy]
    locations: Locations
    already_generated_characters: list[Character]
