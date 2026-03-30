from dataclasses import dataclass

from model.game_context.items import Items
from model.game_context.locations import Locations
from model.mobs.character import Character
from model.mobs.enemy import Enemy


@dataclass
class GameContext:
    setting: str
    items: Items
    enemies: list[Enemy]
    locations: Locations
    already_generated_characters: list[Character]
