from model.player.level_gradation import LevelGradation


def create_levels(xp_list) -> list[LevelGradation]:
    result = []
    
    level = 1
    for xp in xp_list:
        result.append(LevelGradation(level, xp))
    
    return result
    

LEVELS = create_levels([50, 100, 200, 350, 500, 750, 950, 1300, 1800])
