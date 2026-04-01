from attr import asdict, dataclass

from model.game.context.game_objects import GameObjects
from model.mobs.character import Character
from model.player.player import Player


@dataclass
class GameState:
    player: Player
    context: GameObjects
    
    def __dict__(self):
        return asdict(self)
