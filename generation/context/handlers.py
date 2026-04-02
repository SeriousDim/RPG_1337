from functools import wraps
from typing import Any, Callable

from generation.const import PLAYER_KEY, GAME_KEY, QUEST_TYPE_KEY, QUEST_FORMAT_KEY
from model.game.state.game_state import GameState

import yaml

from prompt.mapper.player_mapper import PlayerPromptMapper
from prompt.mapper.quest_mapper import QuestTypeMapper


def _surround_with_yaml_block(func: Callable[..., str]) -> Callable[..., str]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        result = func(*args, **kwargs)
        return f"```yaml\n{result}\n```"
    return wrapper


@_surround_with_yaml_block
def _to_yaml(obj, root_name) -> str:
    return yaml.safe_dump({root_name: obj.__dict__()}, allow_unicode=True)


def handle_player_key(state: GameState) -> Callable[[], str]:
    def result():
        player = state.player
        prompt_player = PlayerPromptMapper.to(player)
        return _to_yaml(prompt_player, "player")
    
    return result


def handle_game_key(state: GameState) -> Callable[[], str]:
    def result():
        game_objects = state.context
        return _to_yaml(game_objects, "game")
    
    return result


def handle_quest_type_key(quest_type: str) -> Callable[[], str]:
    def result():
        return QuestTypeMapper.handle_quest_type_key(quest_type)
    
    return result


def handle_quest_format_key(quest_type: str) -> Callable[[], str]:
    def result():
        return QuestTypeMapper.handle_quest_format_key(quest_type)
    
    return result
