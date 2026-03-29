from model.player.level_gradation import LevelGradation


def create_levels(xp_list) -> list[LevelGradation]:
    result = []
    
    for level, xp in enumerate(xp_list, start=1):
        result.append(LevelGradation(level, xp))
    
    return result
    

LEVELS = create_levels([50, 100, 200, 350, 500, 750, 950, 1300, 1800])

INITIAL_HEALTH: int = 100
INITIAL_MONEY: int = 0
