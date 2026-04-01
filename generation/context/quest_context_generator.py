from generation.const import DELIVERY, GAME_KEY, PLAYER_KEY, QUEST_FORMAT_KEY, QUEST_TYPE_KEY
from generation.context.handlers import handle_game_key, handle_player_key, handle_quest_format_key, handle_quest_type_key
from model.game.state.game_state import GameState

class QuestContextGenerator:
    
    def generate(keys: list[str], state: GameState, quest_type: str) -> dict:
        handlers = {
            PLAYER_KEY: handle_player_key(state),
            GAME_KEY: handle_game_key(state),
            QUEST_TYPE_KEY: handle_quest_type_key(quest_type),
            QUEST_FORMAT_KEY: handle_quest_format_key(quest_type)
        }
        result = {}
        
        for key in keys:
            result[key] = handlers[key]()
        
        return result
