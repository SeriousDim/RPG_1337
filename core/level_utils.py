from model.objects.player import LEVELS
from model.player.level_gradation import LevelGradation


def find_level_gradation(level: int) -> LevelGradation:
    return next(filter(lambda g: g.level == level, LEVELS))

def get_max_possible_level() -> int:
    return max(map(lambda g: g.level, LEVELS))
