from model.game.context.locations import Locations
from model.locations.locations import BufferedLocation, PrimaryLocation
from model.objects.objects import HERBS, ORES


PRIMARY_LOCATIONS = [
    PrimaryLocation("Королевская столица"),
    PrimaryLocation("Деревня Речных Лугов"),
    PrimaryLocation("Лесной Посад"),
    PrimaryLocation("Гномьи Копи"),
    PrimaryLocation("Портовый Град"),
    PrimaryLocation("Древний Монастырь"),
    PrimaryLocation("Пограничная Крепость"),
    PrimaryLocation("Торговый Город"),
    PrimaryLocation("Высокий Замок"),
]


BUFFERED_LOCATIONS = [
    BufferedLocation("Одуванчиковая Поляна", HERBS[0], ORES[0]),
    BufferedLocation("Подорожниковый Бор", HERBS[1], ORES[1]),
    BufferedLocation("Фикусовая Роща", HERBS[2], ORES[2]),
    BufferedLocation("Цитрусовый Сад", HERBS[3], ORES[3]),
    BufferedLocation("Алоевый Каньон", HERBS[4], ORES[4]),
    BufferedLocation("Дубовая Чаща", HERBS[5], ORES[5]),
    BufferedLocation("Баобабовая Долина", HERBS[6], ORES[6]),
    BufferedLocation("Пальмовый Оазис", HERBS[7], ORES[7]),
]


def get_locations() -> Locations:
    return Locations(
        primary=PRIMARY_LOCATIONS,
        buffered=BUFFERED_LOCATIONS,
    )
