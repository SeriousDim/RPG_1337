from attr import asdict, dataclass

from generation.objects.game_objects_generator import GameObjectsGenerator
from generation.objects.player_generator import PlayerGenerator
from model.game.context.game_objects import GameObjects
from model.mobs.character import Character
from model.objects.characters import CHARACTERS
from model.player.player import Player


class GameState:
    player: Player
    context: GameObjects
    
    def __init__(self):
        self.player = PlayerGenerator.create_initial_player()
        self.context = GameObjectsGenerator.create_game_context()
        self.context.already_generated_characters = CHARACTERS
    
    def __dict__(self):
        return asdict(self)
