from model.game.context.game_objects import GameObjects
from prompt.model.game.game_objects import GameObjects as PromptGameObjects


class GamePromptMapper:
    
    @staticmethod
    def to(game: GameObjects) -> PromptGameObjects:
        return PromptGameObjects(game)
