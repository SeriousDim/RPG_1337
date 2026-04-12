from dataclasses import dataclass

from core.level_utils import find_level_gradation, get_max_possible_level
from model.objects.player import LEVELS
from model.player.level_gradation import LevelGradation


@dataclass
class PlayerLevel:
    current_level: int
    current_xp: int
    xp_to_next_level: int
    max_possible_level: int
    
    def __init__(self, level: int, current_xp = 0):
        gradation = find_level_gradation(level)
        
        self.current_level = gradation.level
        self.current_xp = current_xp
        self.xp_to_next_level = gradation.xp_to_next_level
        self.max_possible_level = get_max_possible_level()
    
    def to_dict(self):
        return {
            "current_level": self.current_level,
            "current_xp": self.current_xp,
            "xp_to_next_level": self.xp_to_next_level,
            "max_possible_level": self.max_possible_level
        }
