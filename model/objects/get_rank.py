from model.objects.objects import MAX_RANKS


def get_max_rank(type: str):
    if type in MAX_RANKS.keys:
        return MAX_RANKS[type]
    raise ValueError("No such item type: {type}")
