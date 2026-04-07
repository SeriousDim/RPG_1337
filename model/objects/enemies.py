from model.common.health import Health
from model.mobs.enemy import Enemy


ENEMIES = [
    Enemy("Лесной разбойник", 1, Health(28, 28), 4, 5),
    Enemy("Гоблин-вор", 1, Health(24, 24), 3, 4),
    Enemy("Пещерная крыса", 1, Health(20, 20), 2, 3),
    Enemy("Болотный слизень", 2, Health(38, 38), 5, 7),
    Enemy("Скелет-ополченец", 2, Health(44, 44), 6, 9),
    Enemy("Дикарь с дубиной", 3, Health(56, 56), 8, 12),
    Enemy("Волк-альфа", 3, Health(52, 52), 7, 12),
    Enemy("Орк-налётчик", 4, Health(72, 72), 10, 18),
    Enemy("Разбойник в стальной броне", 4, Health(78, 78), 11, 20),
    Enemy("Костяной рыцарь", 5, Health(96, 96), 13, 26),
    Enemy("Тролль камнедробитель", 5, Health(110, 110), 15, 30),
    Enemy("Маг огня", 6, Health(124, 124), 18, 40),
    Enemy("Элитный страж рубина", 7, Health(142, 142), 21, 55),
    Enemy("Драконий всадник", 8, Health(170, 170), 25, 75),
    Enemy("Древний лич", 10, Health(220, 220), 32, 120),
]


def get_enemy_names() -> list[str]:
    return list(map(lambda e: e.name, ENEMIES))
