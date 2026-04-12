from dataclasses import dataclass

from prompt.model.game.items import Items
from prompt.model.game.character import Character
from prompt.model.game.enemy import Enemy
from prompt.model.game.locations import Locations
from model.game.context.game_objects import GameObjects as ModelGameObjects


@dataclass
class GameObjects:
    setting: str
    items: Items
    enemies: list[Enemy]
    locations: Locations
    already_generated_characters: list[Character]
    
    def __init__(self, game_objects: ModelGameObjects):
        self.setting = game_objects.setting
        self.items = Items(game_objects.items)
        self.enemies = [Enemy(enemy) for enemy in game_objects.enemies]
        self.locations = Locations(game_objects.locations)
        self.already_generated_characters = [Character(char) for char in game_objects.already_generated_characters]
    
    def to_dict(self):
        return {
            "setting": self.setting,
            "items": self.items.to_dict(),
            "enemies": [enemy.to_dict() for enemy in self.enemies],
            "locations": self.locations.to_dict(),
            "already_generated_characters": [char.to_dict() for char in self.already_generated_characters]
        }