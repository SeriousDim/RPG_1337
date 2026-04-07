from model.game.context.armors import Armors
from model.items.armor import Armor


HELMETS = [
    Armor(1, "Деревянный шлем", "шлем", 1),
    Armor(2, "Железный шлем", "шлем", 3),
    Armor(3, "Позолоченный шлем", "шлем", 7)
]

CHEST_PLATES = [
    Armor(1, "Деревянный нагрудник", "нагрудник", 2),
    Armor(2, "Железный нагрудник", "нагрудник", 4),
    Armor(3, "Позолоченный нагрудник", "нагрудник", 7),
    Armor(4, "Нагрудник с рубином", "нагрудник", 12),
    Armor(5, "Нагрудник с изумрудом", "нагрудник", 17),
    Armor(6, "Нагрудник с бриллиантом", "нагрудник", 20)
]

LEGGINGS = [
    Armor(1, "Деревянные штаны", "штаны", 1),
    Armor(2, "Железные штаны", "штаны", 3),
    Armor(3, "Позолоченные штаны", "штаны", 6),
    Armor(4, "Штаны с изумрудом", "штаны", 10)
]

SHIELDS = [
    Armor(1, "Деревянный щит", "щит", 2),
    Armor(2, "Железный щит", "щит", 4),
    Armor(3, "Позолоченный щит", "щит", 6),
    Armor(4, "Щит с рубином", "щит", 8),
    Armor(5, "Щит с изумрудом", "щит", 9),
    Armor(6, "Щит с бриллиантом", "щит", 10)
]

MAX_RANKS = {
    'шлем': len(HELMETS),
    'нагрудник': len(CHEST_PLATES),
    'штаны': len(LEGGINGS),
    'щит': len(SHIELDS),
}

def get_armors() -> Armors:
    return Armors(
        helmets=HELMETS,
        chestplates=CHEST_PLATES,
        leggings=LEGGINGS,
        shields=SHIELDS
    )


def get_armor_names() -> list[str]:
    return list(map(lambda a: a.name, HELMETS + CHEST_PLATES + LEGGINGS + SHIELDS))


def find_any_armor_by_name(name: str) -> Armor:
    filtered = list(filter(lambda a: a.name == name, HELMETS + CHEST_PLATES + LEGGINGS + SHIELDS))
    if len(filtered) > 0:
        return filtered[0]
    
    return None