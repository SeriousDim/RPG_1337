from model.objects.enemies import ENEMIES
from model.objects.objects import MAX_RANKS as OBJECTS_MAX_RANKS
from model.objects.armors import MAX_RANKS as ARMOR_MAX_RANKS


def get_max_rank(type: str):
    if type in OBJECTS_MAX_RANKS.keys():
        return OBJECTS_MAX_RANKS[type]
    if type in ARMOR_MAX_RANKS.keys():
        return ARMOR_MAX_RANKS[type]
    raise ValueError(f"No such item type: {type}")


def get_max_enemy_rank():
    return max(map(lambda e: e.rank, ENEMIES))
