from model.items.instrument import Instrument
from model.items.resource import Resource, ResourceType
from model.items.sword import Sword


SWORDS = [
    Sword(1, "Деревянный меч", 2, 1),
    Sword(2, "Каменный меч", 4, 1),
    Sword(3, "Железный меч", 6, 1),
    Sword(4, "Стальной меч", 5, 2),
    Sword(5, "Позолоченный меч", 8, 2),
    Sword(6, "Меч с лазуритом", 12, 2),
    Sword(7, "Меч с рубином", 9, 3),
    Sword(8, "Меч с изумрудом", 15, 3),
    Sword(9, "Меч с бриллиантом", 19, 3),
    Sword(10, "Меч властелина", 17, 4)
]

HERBS = [
    Resource(1, "Одуванчик", ResourceType.HERB, 1),
    Resource(2, "Подорожник", ResourceType.HERB, 1),
    Resource(3, "Фикус", ResourceType.HERB, 2),
    Resource(4, "Цитрус", ResourceType.HERB, 2),
    Resource(5, "Алоэ", ResourceType.HERB, 2),
    Resource(6, "Дуб", ResourceType.HERB, 3),
    Resource(7, "Баобаб", ResourceType.HERB, 3),
    Resource(8, "Пальма", ResourceType.HERB, 3),
]

ORES = [
    Resource(1, "Уголь", ResourceType.ORE, 1),
    Resource(2, "Железо", ResourceType.ORE, 1),
    Resource(3, "Олово", ResourceType.ORE, 2),
    Resource(4, "Золото", ResourceType.ORE, 2),
    Resource(5, "Лазурит", ResourceType.ORE, 2),
    Resource(6, "Рубин", ResourceType.ORE, 3),
    Resource(7, "Изумруд", ResourceType.ORE, 3),
    Resource(8, "Бриллиант", ResourceType.ORE, 3),
]

SHOVELS = [
    Instrument(1, "Деревянная лопата", "лопата"),
    Instrument(2, "Железная лопата", "лопата"),
    Instrument(3, "Лопата с лазуритом", "лопата")
]

PICKAXES = [
    Instrument(1, "Деревянная кирка", "кирка"),
    Instrument(2, "Железная кирка", "кирка"),
    Instrument(3, "Кирка с лазуритом", "кирка")
]

MAX_RANKS = {
    'оружие': len(SWORDS),
    'трава': len(HERBS),
    'руда': len(ORES),
    'лопата': len(SHOVELS),
    'кирка': len(PICKAXES)
}
