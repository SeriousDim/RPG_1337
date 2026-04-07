from model.mobs.character import Character
from model.objects.objects import SWORDS, SHOVELS, PICKAXES, HERBS, ORES
from model.objects.locations import PRIMARY_LOCATIONS


CHARACTERS = [
    Character(
        name="Гаррик Кузнец",
        location=PRIMARY_LOCATIONS[0],
        items_can_give_after_quest_finished=[SWORDS[0], SHOVELS[0], PICKAXES[0]],
        items_can_be_accepted_for_delivery_or_collection=[HERBS[0], ORES[0]]
    ),
    Character(
        name="Лира Лекарь",
        location=PRIMARY_LOCATIONS[1],
        items_can_give_after_quest_finished=[SWORDS[1], SHOVELS[1]],
        items_can_be_accepted_for_delivery_or_collection=[HERBS[1], ORES[1]]
    ),
    Character(
        name="Бром Топор",
        location=PRIMARY_LOCATIONS[2],
        items_can_give_after_quest_finished=[SWORDS[2], PICKAXES[1]],
        items_can_be_accepted_for_delivery_or_collection=[HERBS[2], ORES[2]]
    ),
    Character(
        name="Джонас Шахтер",
        location=PRIMARY_LOCATIONS[3],
        items_can_give_after_quest_finished=[SWORDS[3], SHOVELS[2]],
        items_can_be_accepted_for_delivery_or_collection=[HERBS[3], ORES[3]]
    ),
    Character(
        name="Капитан Морант",
        location=PRIMARY_LOCATIONS[4],
        items_can_give_after_quest_finished=[SWORDS[4], PICKAXES[2]],
        items_can_be_accepted_for_delivery_or_collection=[HERBS[4], ORES[4]]
    ),
    Character(
        name="Отшельник Элрон",
        location=PRIMARY_LOCATIONS[5],
        items_can_give_after_quest_finished=[SWORDS[5]],
        items_can_be_accepted_for_delivery_or_collection=[HERBS[5], ORES[5]]
    ),
    Character(
        name="Рыцарь Валтер",
        location=PRIMARY_LOCATIONS[6],
        items_can_give_after_quest_finished=[SWORDS[6]],
        items_can_be_accepted_for_delivery_or_collection=[HERBS[6], ORES[6]]
    ),
    Character(
        name="Купец Орма",
        location=PRIMARY_LOCATIONS[7],
        items_can_give_after_quest_finished=[SWORDS[7]],
        items_can_be_accepted_for_delivery_or_collection=[HERBS[7], ORES[7]]
    ),
    Character(
        name="Лорд Дрейк",
        location=PRIMARY_LOCATIONS[8],
        items_can_give_after_quest_finished=[SWORDS[8]],
        items_can_be_accepted_for_delivery_or_collection=[SWORDS[9], HERBS[0], ORES[0]]
    ),
    Character(
        name="Мастер Ювелир",
        location=PRIMARY_LOCATIONS[0],
        items_can_give_after_quest_finished=[SWORDS[4], SWORDS[5]],
        items_can_be_accepted_for_delivery_or_collection=[ORES[5]]
    ),
    Character(
        name="Травница Марта",
        location=PRIMARY_LOCATIONS[1],
        items_can_give_after_quest_finished=[SWORDS[1], SWORDS[2]],
        items_can_be_accepted_for_delivery_or_collection=[HERBS[2], HERBS[3]]
    ),
    Character(
        name="Лесничий Грум",
        location=PRIMARY_LOCATIONS[2],
        items_can_give_after_quest_finished=[SWORDS[3], SHOVELS[1]],
        items_can_be_accepted_for_delivery_or_collection=[HERBS[4], HERBS[5]]
    ),
    Character(
        name="Гном Брок",
        location=PRIMARY_LOCATIONS[3],
        items_can_give_after_quest_finished=[SWORDS[6], PICKAXES[1]],
        items_can_be_accepted_for_delivery_or_collection=[ORES[1], ORES[2]]
    ),
    Character(
        name="Капитан Лира",
        location=PRIMARY_LOCATIONS[4],
        items_can_give_after_quest_finished=[SWORDS[7], SHOVELS[2]],
        items_can_be_accepted_for_delivery_or_collection=[ORES[3], ORES[4]]
    ),
    Character(
        name="Монах Тибор",
        location=PRIMARY_LOCATIONS[5],
        items_can_give_after_quest_finished=[SWORDS[0], SWORDS[8]],
        items_can_be_accepted_for_delivery_or_collection=[HERBS[6], HERBS[7]]
    ),
    Character(
        name="Сержант Келл",
        location=PRIMARY_LOCATIONS[6],
        items_can_give_after_quest_finished=[SWORDS[2], SWORDS[5]],
        items_can_be_accepted_for_delivery_or_collection=[HERBS[1], ORES[6]]
    ),
    Character(
        name="Торговец Нарек",
        location=PRIMARY_LOCATIONS[7],
        items_can_give_after_quest_finished=[SWORDS[3], SWORDS[4]],
        items_can_be_accepted_for_delivery_or_collection=[HERBS[0], HERBS[7]]
    ),
    Character(
        name="Страж Замка",
        location=PRIMARY_LOCATIONS[8],
        items_can_give_after_quest_finished=[SWORDS[1], SWORDS[6]],
        items_can_be_accepted_for_delivery_or_collection=[HERBS[3], ORES[1]]
    ),
    Character(
        name="Кузнец Роган",
        location=PRIMARY_LOCATIONS[0],
        items_can_give_after_quest_finished=[SWORDS[7], SWORDS[9]],
        items_can_be_accepted_for_delivery_or_collection=[ORES[2], ORES[7]]
    ),
    Character(
        name="Целительница Алина",
        location=PRIMARY_LOCATIONS[5],
        items_can_give_after_quest_finished=[SWORDS[5], SWORDS[8]],
        items_can_be_accepted_for_delivery_or_collection=[HERBS[4], HERBS[5], ORES[0]]
    )
]

def get_character_names():
    return list(map(lambda c: c.name, CHARACTERS))


def find_character_by_name(name):
    return list(filter(lambda c: c.name == name, CHARACTERS))[0]
