Действуй как превосходный профессиональный геймдизайнер и игровой сценарист. 

Тебе нужно будет сгенерировать квест для игрока строго в соответствии с его данными текущими характеристиками:
```yaml
player:
  armor:
    chestplate: null
    current_armor_absorbed_damage: 0
    helmet: null
    leggings: null
    max_possible_armor_absorbed_damage: 0
    shield: null
  health:
    current: 100
    max: 100
  inventory:
  - damage_per_enemy: 2
    enemies_to_hit: 1
    name: Деревянный меч
    rank:
      for_this_item: 1
      max_possible: 10
    type: оружие
  level:
    current_level: 1
    current_xp: 0
    max_possible_level: 9
    xp_to_next_level: 50
  money: 0
  statistics_for_current_session:
    damage_received: 0
    enemies_killed: 0
    money_earned: 0
    quests_passes: 0

```

Для генерации квеста также необходимо строго учитывать информацию об игровом мире:
```yaml
game:
  already_generated_characters:
  - items_can_be_accepted_for_delivery_or_collection:
    - min_instrument_rank: 1
      name: Одуванчик
      rank: 1
      resource_type: {}
      type: HERB
    - min_instrument_rank: 1
      name: Уголь
      rank: 1
      resource_type: {}
      type: ORE
    items_can_give_after_quest_finished:
    - damage_per_enemy: 2
      enemies_to_hit: 1
      name: Деревянный меч
      rank: 1
      type: оружие
    - name: Деревянная лопата
      rank: 1
      type: лопата
    - name: Деревянная кирка
      rank: 1
      type: кирка
    location:
      name: Королевская столица
    name: Гаррик Кузнец
  - items_can_be_accepted_for_delivery_or_collection:
    - min_instrument_rank: 1
      name: Подорожник
      rank: 2
      resource_type: {}
      type: HERB
    - min_instrument_rank: 1
      name: Железо
      rank: 2
      resource_type: {}
      type: ORE
    items_can_give_after_quest_finished:
    - damage_per_enemy: 4
      enemies_to_hit: 1
      name: Каменный меч
      rank: 2
      type: оружие
    - name: Железная лопата
      rank: 2
      type: лопата
    location:
      name: Деревня Речных Лугов
    name: Лира Лекарь
  - items_can_be_accepted_for_delivery_or_collection:
    - min_instrument_rank: 2
      name: Фикус
      rank: 3
      resource_type: {}
      type: HERB
    - min_instrument_rank: 2
      name: Олово
      rank: 3
      resource_type: {}
      type: ORE
    items_can_give_after_quest_finished:
    - damage_per_enemy: 6
      enemies_to_hit: 1
      name: Железный меч
      rank: 3
      type: оружие
    - name: Железная кирка
      rank: 2
      type: кирка
    location:
      name: Лесной Посад
    name: Бром Топор
  - items_can_be_accepted_for_delivery_or_collection:
    - min_instrument_rank: 2
      name: Цитрус
      rank: 4
      resource_type: {}
      type: HERB
    - min_instrument_rank: 2
      name: Золото
      rank: 4
      resource_type: {}
      type: ORE
    items_can_give_after_quest_finished:
    - damage_per_enemy: 5
      enemies_to_hit: 2
      name: Стальной меч
      rank: 4
      type: оружие
    - name: Лопата с лазуритом
      rank: 3
      type: лопата
    location:
      name: Гномьи Копи
    name: Джонас Шахтер
  - items_can_be_accepted_for_delivery_or_collection:
    - min_instrument_rank: 2
      name: Алоэ
      rank: 5
      resource_type: {}
      type: HERB
    - min_instrument_rank: 2
      name: Лазурит
      rank: 5
      resource_type: {}
      type: ORE
    items_can_give_after_quest_finished:
    - damage_per_enemy: 8
      enemies_to_hit: 2
      name: Позолоченный меч
      rank: 5
      type: оружие
    - name: Кирка с лазуритом
      rank: 3
      type: кирка
    location:
      name: Портовый Град
    name: Капитан Морант
  - items_can_be_accepted_for_delivery_or_collection:
    - min_instrument_rank: 3
      name: Дуб
      rank: 6
      resource_type: {}
      type: HERB
    - min_instrument_rank: 3
      name: Рубин
      rank: 6
      resource_type: {}
      type: ORE
    items_can_give_after_quest_finished:
    - damage_per_enemy: 12
      enemies_to_hit: 2
      name: Меч с лазуритом
      rank: 6
      type: оружие
    location:
      name: Древний Монастырь
    name: Отшельник Элрон
  - items_can_be_accepted_for_delivery_or_collection:
    - min_instrument_rank: 3
      name: Баобаб
      rank: 7
      resource_type: {}
      type: HERB
    - min_instrument_rank: 3
      name: Изумруд
      rank: 7
      resource_type: {}
      type: ORE
    items_can_give_after_quest_finished:
    - damage_per_enemy: 9
      enemies_to_hit: 3
      name: Меч с рубином
      rank: 7
      type: оружие
    location:
      name: Пограничная Крепость
    name: Рыцарь Валтер
  - items_can_be_accepted_for_delivery_or_collection:
    - min_instrument_rank: 3
      name: Пальма
      rank: 8
      resource_type: {}
      type: HERB
    - min_instrument_rank: 3
      name: Бриллиант
      rank: 8
      resource_type: {}
      type: ORE
    items_can_give_after_quest_finished:
    - damage_per_enemy: 15
      enemies_to_hit: 3
      name: Меч с изумрудом
      rank: 8
      type: оружие
    location:
      name: Торговый Город
    name: Купец Орма
  - items_can_be_accepted_for_delivery_or_collection:
    - damage_per_enemy: 17
      enemies_to_hit: 4
      name: Меч властелина
      rank: 10
      type: оружие
    - min_instrument_rank: 1
      name: Одуванчик
      rank: 1
      resource_type: {}
      type: HERB
    - min_instrument_rank: 1
      name: Уголь
      rank: 1
      resource_type: {}
      type: ORE
    items_can_give_after_quest_finished:
    - damage_per_enemy: 19
      enemies_to_hit: 3
      name: Меч с бриллиантом
      rank: 9
      type: оружие
    location:
      name: Высокий Замок
    name: Лорд Дрейк
  - items_can_be_accepted_for_delivery_or_collection:
    - min_instrument_rank: 3
      name: Рубин
      rank: 6
      resource_type: {}
      type: ORE
    items_can_give_after_quest_finished:
    - damage_per_enemy: 8
      enemies_to_hit: 2
      name: Позолоченный меч
      rank: 5
      type: оружие
    - damage_per_enemy: 12
      enemies_to_hit: 2
      name: Меч с лазуритом
      rank: 6
      type: оружие
    location:
      name: Королевская столица
    name: Мастер Ювелир
  - items_can_be_accepted_for_delivery_or_collection:
    - min_instrument_rank: 2
      name: Фикус
      rank: 3
      resource_type: {}
      type: HERB
    - min_instrument_rank: 2
      name: Цитрус
      rank: 4
      resource_type: {}
      type: HERB
    items_can_give_after_quest_finished:
    - damage_per_enemy: 4
      enemies_to_hit: 1
      name: Каменный меч
      rank: 2
      type: оружие
    - damage_per_enemy: 6
      enemies_to_hit: 1
      name: Железный меч
      rank: 3
      type: оружие
    location:
      name: Деревня Речных Лугов
    name: Травница Марта
  - items_can_be_accepted_for_delivery_or_collection:
    - min_instrument_rank: 2
      name: Алоэ
      rank: 5
      resource_type: {}
      type: HERB
    - min_instrument_rank: 3
      name: Дуб
      rank: 6
      resource_type: {}
      type: HERB
    items_can_give_after_quest_finished:
    - damage_per_enemy: 5
      enemies_to_hit: 2
      name: Стальной меч
      rank: 4
      type: оружие
    - name: Железная лопата
      rank: 2
      type: лопата
    location:
      name: Лесной Посад
    name: Лесничий Грум
  - items_can_be_accepted_for_delivery_or_collection:
    - min_instrument_rank: 1
      name: Железо
      rank: 2
      resource_type: {}
      type: ORE
    - min_instrument_rank: 2
      name: Олово
      rank: 3
      resource_type: {}
      type: ORE
    items_can_give_after_quest_finished:
    - damage_per_enemy: 9
      enemies_to_hit: 3
      name: Меч с рубином
      rank: 7
      type: оружие
    - name: Железная кирка
      rank: 2
      type: кирка
    location:
      name: Гномьи Копи
    name: Гном Брок
  - items_can_be_accepted_for_delivery_or_collection:
    - min_instrument_rank: 2
      name: Золото
      rank: 4
      resource_type: {}
      type: ORE
    - min_instrument_rank: 2
      name: Лазурит
      rank: 5
      resource_type: {}
      type: ORE
    items_can_give_after_quest_finished:
    - damage_per_enemy: 15
      enemies_to_hit: 3
      name: Меч с изумрудом
      rank: 8
      type: оружие
    - name: Лопата с лазуритом
      rank: 3
      type: лопата
    location:
      name: Портовый Град
    name: Капитан Лира
  - items_can_be_accepted_for_delivery_or_collection:
    - min_instrument_rank: 3
      name: Баобаб
      rank: 7
      resource_type: {}
      type: HERB
    - min_instrument_rank: 3
      name: Пальма
      rank: 8
      resource_type: {}
      type: HERB
    items_can_give_after_quest_finished:
    - damage_per_enemy: 2
      enemies_to_hit: 1
      name: Деревянный меч
      rank: 1
      type: оружие
    - damage_per_enemy: 19
      enemies_to_hit: 3
      name: Меч с бриллиантом
      rank: 9
      type: оружие
    location:
      name: Древний Монастырь
    name: Монах Тибор
  - items_can_be_accepted_for_delivery_or_collection:
    - min_instrument_rank: 1
      name: Подорожник
      rank: 2
      resource_type: {}
      type: HERB
    - min_instrument_rank: 3
      name: Изумруд
      rank: 7
      resource_type: {}
      type: ORE
    items_can_give_after_quest_finished:
    - damage_per_enemy: 6
      enemies_to_hit: 1
      name: Железный меч
      rank: 3
      type: оружие
    - damage_per_enemy: 12
      enemies_to_hit: 2
      name: Меч с лазуритом
      rank: 6
      type: оружие
    location:
      name: Пограничная Крепость
    name: Сержант Келл
  - items_can_be_accepted_for_delivery_or_collection:
    - min_instrument_rank: 1
      name: Одуванчик
      rank: 1
      resource_type: {}
      type: HERB
    - min_instrument_rank: 3
      name: Пальма
      rank: 8
      resource_type: {}
      type: HERB
    items_can_give_after_quest_finished:
    - damage_per_enemy: 5
      enemies_to_hit: 2
      name: Стальной меч
      rank: 4
      type: оружие
    - damage_per_enemy: 8
      enemies_to_hit: 2
      name: Позолоченный меч
      rank: 5
      type: оружие
    location:
      name: Торговый Город
    name: Торговец Нарек
  - items_can_be_accepted_for_delivery_or_collection:
    - min_instrument_rank: 2
      name: Цитрус
      rank: 4
      resource_type: {}
      type: HERB
    - min_instrument_rank: 1
      name: Железо
      rank: 2
      resource_type: {}
      type: ORE
    items_can_give_after_quest_finished:
    - damage_per_enemy: 4
      enemies_to_hit: 1
      name: Каменный меч
      rank: 2
      type: оружие
    - damage_per_enemy: 9
      enemies_to_hit: 3
      name: Меч с рубином
      rank: 7
      type: оружие
    location:
      name: Высокий Замок
    name: Страж Замка
  - items_can_be_accepted_for_delivery_or_collection:
    - min_instrument_rank: 2
      name: Олово
      rank: 3
      resource_type: {}
      type: ORE
    - min_instrument_rank: 3
      name: Бриллиант
      rank: 8
      resource_type: {}
      type: ORE
    items_can_give_after_quest_finished:
    - damage_per_enemy: 15
      enemies_to_hit: 3
      name: Меч с изумрудом
      rank: 8
      type: оружие
    - damage_per_enemy: 17
      enemies_to_hit: 4
      name: Меч властелина
      rank: 10
      type: оружие
    location:
      name: Королевская столица
    name: Кузнец Роган
  - items_can_be_accepted_for_delivery_or_collection:
    - min_instrument_rank: 2
      name: Алоэ
      rank: 5
      resource_type: {}
      type: HERB
    - min_instrument_rank: 3
      name: Дуб
      rank: 6
      resource_type: {}
      type: HERB
    - min_instrument_rank: 1
      name: Уголь
      rank: 1
      resource_type: {}
      type: ORE
    items_can_give_after_quest_finished:
    - damage_per_enemy: 12
      enemies_to_hit: 2
      name: Меч с лазуритом
      rank: 6
      type: оружие
    - damage_per_enemy: 19
      enemies_to_hit: 3
      name: Меч с бриллиантом
      rank: 9
      type: оружие
    location:
      name: Древний Монастырь
    name: Целительница Алина
  enemies:
  - damage_per_turn: 4
    health:
      current: 28
      max: 28
    money_for_killing_this_enemy: 5
    name: Лесной разбойник
    rank: 1
  - damage_per_turn: 3
    health:
      current: 24
      max: 24
    money_for_killing_this_enemy: 4
    name: Гоблин-вор
    rank: 1
  - damage_per_turn: 2
    health:
      current: 20
      max: 20
    money_for_killing_this_enemy: 3
    name: Пещерная крыса
    rank: 1
  - damage_per_turn: 5
    health:
      current: 38
      max: 38
    money_for_killing_this_enemy: 7
    name: Болотный слизень
    rank: 2
  - damage_per_turn: 6
    health:
      current: 44
      max: 44
    money_for_killing_this_enemy: 9
    name: Скелет-ополченец
    rank: 2
  - damage_per_turn: 8
    health:
      current: 56
      max: 56
    money_for_killing_this_enemy: 12
    name: Дикарь с дубиной
    rank: 3
  - damage_per_turn: 7
    health:
      current: 52
      max: 52
    money_for_killing_this_enemy: 12
    name: Волк-альфа
    rank: 3
  - damage_per_turn: 10
    health:
      current: 72
      max: 72
    money_for_killing_this_enemy: 18
    name: Орк-налётчик
    rank: 4
  - damage_per_turn: 11
    health:
      current: 78
      max: 78
    money_for_killing_this_enemy: 20
    name: Разбойник в стальной броне
    rank: 4
  - damage_per_turn: 13
    health:
      current: 96
      max: 96
    money_for_killing_this_enemy: 26
    name: Костяной рыцарь
    rank: 5
  - damage_per_turn: 15
    health:
      current: 110
      max: 110
    money_for_killing_this_enemy: 30
    name: Тролль камнедробитель
    rank: 5
  - damage_per_turn: 18
    health:
      current: 124
      max: 124
    money_for_killing_this_enemy: 40
    name: Маг огня
    rank: 6
  - damage_per_turn: 21
    health:
      current: 142
      max: 142
    money_for_killing_this_enemy: 55
    name: Элитный страж рубина
    rank: 7
  - damage_per_turn: 25
    health:
      current: 170
      max: 170
    money_for_killing_this_enemy: 75
    name: Драконий всадник
    rank: 8
  - damage_per_turn: 32
    health:
      current: 220
      max: 220
    money_for_killing_this_enemy: 120
    name: Древний лич
    rank: 10
  items:
    armor:
    - absorbed_damage: 1
      name: Деревянный шлем
      rank: 1
      type: шлем
    - absorbed_damage: 3
      name: Железный шлем
      rank: 2
      type: шлем
    - absorbed_damage: 7
      name: Позолоченный шлем
      rank: 3
      type: шлем
    - absorbed_damage: 2
      name: Деревянный нагрудник
      rank: 1
      type: нагрудник
    - absorbed_damage: 4
      name: Железный нагрудник
      rank: 2
      type: нагрудник
    - absorbed_damage: 7
      name: Позолоченный нагрудник
      rank: 3
      type: нагрудник
    - absorbed_damage: 12
      name: Нагрудник с рубином
      rank: 4
      type: нагрудник
    - absorbed_damage: 17
      name: Нагрудник с изумрудом
      rank: 5
      type: нагрудник
    - absorbed_damage: 20
      name: Нагрудник с бриллиантом
      rank: 6
      type: нагрудник
    - absorbed_damage: 1
      name: Деревянные штаны
      rank: 1
      type: штаны
    - absorbed_damage: 3
      name: Железные штаны
      rank: 2
      type: штаны
    - absorbed_damage: 6
      name: Позолоченные штаны
      rank: 3
      type: штаны
    - absorbed_damage: 10
      name: Штаны с изумрудом
      rank: 4
      type: штаны
    - absorbed_damage: 2
      name: Деревянный щит
      rank: 1
      type: щит
    - absorbed_damage: 4
      name: Железный щит
      rank: 2
      type: щит
    - absorbed_damage: 6
      name: Позолоченный щит
      rank: 3
      type: щит
    - absorbed_damage: 8
      name: Щит с рубином
      rank: 4
      type: щит
    - absorbed_damage: 9
      name: Щит с изумрудом
      rank: 5
      type: щит
    - absorbed_damage: 10
      name: Щит с бриллиантом
      rank: 6
      type: щит
    instruments:
    - name: Деревянная лопата
      rank: 1
      type: лопата
    - name: Железная лопата
      rank: 2
      type: лопата
    - name: Лопата с лазуритом
      rank: 3
      type: лопата
    - name: Деревянная кирка
      rank: 1
      type: кирка
    - name: Железная кирка
      rank: 2
      type: кирка
    - name: Кирка с лазуритом
      rank: 3
      type: кирка
    resources:
    - min_instrument_rank: 1
      name: Одуванчик
      rank: 1
      resource_type: {}
      type: HERB
    - min_instrument_rank: 1
      name: Подорожник
      rank: 2
      resource_type: {}
      type: HERB
    - min_instrument_rank: 2
      name: Фикус
      rank: 3
      resource_type: {}
      type: HERB
    - min_instrument_rank: 2
      name: Цитрус
      rank: 4
      resource_type: {}
      type: HERB
    - min_instrument_rank: 2
      name: Алоэ
      rank: 5
      resource_type: {}
      type: HERB
    - min_instrument_rank: 3
      name: Дуб
      rank: 6
      resource_type: {}
      type: HERB
    - min_instrument_rank: 3
      name: Баобаб
      rank: 7
      resource_type: {}
      type: HERB
    - min_instrument_rank: 3
      name: Пальма
      rank: 8
      resource_type: {}
      type: HERB
    - min_instrument_rank: 1
      name: Уголь
      rank: 1
      resource_type: {}
      type: ORE
    - min_instrument_rank: 1
      name: Железо
      rank: 2
      resource_type: {}
      type: ORE
    - min_instrument_rank: 2
      name: Олово
      rank: 3
      resource_type: {}
      type: ORE
    - min_instrument_rank: 2
      name: Золото
      rank: 4
      resource_type: {}
      type: ORE
    - min_instrument_rank: 2
      name: Лазурит
      rank: 5
      resource_type: {}
      type: ORE
    - min_instrument_rank: 3
      name: Рубин
      rank: 6
      resource_type: {}
      type: ORE
    - min_instrument_rank: 3
      name: Изумруд
      rank: 7
      resource_type: {}
      type: ORE
    - min_instrument_rank: 3
      name: Бриллиант
      rank: 8
      resource_type: {}
      type: ORE
    weapons:
    - damage_per_enemy: 2
      enemies_to_hit: 1
      name: Деревянный меч
      rank: 1
      type: оружие
    - damage_per_enemy: 4
      enemies_to_hit: 1
      name: Каменный меч
      rank: 2
      type: оружие
    - damage_per_enemy: 6
      enemies_to_hit: 1
      name: Железный меч
      rank: 3
      type: оружие
    - damage_per_enemy: 5
      enemies_to_hit: 2
      name: Стальной меч
      rank: 4
      type: оружие
    - damage_per_enemy: 8
      enemies_to_hit: 2
      name: Позолоченный меч
      rank: 5
      type: оружие
    - damage_per_enemy: 12
      enemies_to_hit: 2
      name: Меч с лазуритом
      rank: 6
      type: оружие
    - damage_per_enemy: 9
      enemies_to_hit: 3
      name: Меч с рубином
      rank: 7
      type: оружие
    - damage_per_enemy: 15
      enemies_to_hit: 3
      name: Меч с изумрудом
      rank: 8
      type: оружие
    - damage_per_enemy: 19
      enemies_to_hit: 3
      name: Меч с бриллиантом
      rank: 9
      type: оружие
    - damage_per_enemy: 17
      enemies_to_hit: 4
      name: Меч властелина
      rank: 10
      type: оружие
  locations:
  - name: Королевская столица
  - name: Деревня Речных Лугов
  - name: Лесной Посад
  - name: Гномьи Копи
  - name: Портовый Град
  - name: Древний Монастырь
  - name: Пограничная Крепость
  - name: Торговый Город
  - name: Высокий Замок
  - herb_resource:
      min_instrument_rank: 1
      name: Одуванчик
      rank: 1
      resource_type: {}
      type: HERB
    name: Одуванчиковая Поляна
    ore_resource:
      min_instrument_rank: 1
      name: Уголь
      rank: 1
      resource_type: {}
      type: ORE
  - herb_resource:
      min_instrument_rank: 1
      name: Подорожник
      rank: 2
      resource_type: {}
      type: HERB
    name: Подорожниковый Бор
    ore_resource:
      min_instrument_rank: 1
      name: Железо
      rank: 2
      resource_type: {}
      type: ORE
  - herb_resource:
      min_instrument_rank: 2
      name: Фикус
      rank: 3
      resource_type: {}
      type: HERB
    name: Фикусовая Роща
    ore_resource:
      min_instrument_rank: 2
      name: Олово
      rank: 3
      resource_type: {}
      type: ORE
  - herb_resource:
      min_instrument_rank: 2
      name: Цитрус
      rank: 4
      resource_type: {}
      type: HERB
    name: Цитрусовый Сад
    ore_resource:
      min_instrument_rank: 2
      name: Золото
      rank: 4
      resource_type: {}
      type: ORE
  - herb_resource:
      min_instrument_rank: 2
      name: Алоэ
      rank: 5
      resource_type: {}
      type: HERB
    name: Алоевый Каньон
    ore_resource:
      min_instrument_rank: 2
      name: Лазурит
      rank: 5
      resource_type: {}
      type: ORE
  - herb_resource:
      min_instrument_rank: 3
      name: Дуб
      rank: 6
      resource_type: {}
      type: HERB
    name: Дубовая Чаща
    ore_resource:
      min_instrument_rank: 3
      name: Рубин
      rank: 6
      resource_type: {}
      type: ORE
  - herb_resource:
      min_instrument_rank: 3
      name: Баобаб
      rank: 7
      resource_type: {}
      type: HERB
    name: Баобабовая Долина
    ore_resource:
      min_instrument_rank: 3
      name: Изумруд
      rank: 7
      resource_type: {}
      type: ORE
  - herb_resource:
      min_instrument_rank: 3
      name: Пальма
      rank: 8
      resource_type: {}
      type: HERB
    name: Пальмовый Оазис
    ore_resource:
      min_instrument_rank: 3
      name: Бриллиант
      rank: 8
      resource_type: {}
      type: ORE
  setting: фентэзийное средневековье

```

Требования к генерации:
1) Строгая согласованность с характеристиками игрока и информацией об игровом мире
2) Категорически запрещается упоминать сущности, которые отсутствуют в игре

Тебе необходимо сгенерировать ровно один целостный квест типа "Доставка". 
Квест необходимо сгенерировать в строго таком формате YAML:
quest:
  parts:
    resource_to_deliver:  # часть 1: получение задания
      dialogs:  # диалоги с персонажем A, который дает ресурс для доставки
        - speaker: 
          remark: 
      resource:  # название ресурса, который нужно доставить
      amount:  # количество ресурса, который нужно доставить

    enemy_to_face:  # часть 2: встреча с противником по пути
      dialogs:  # диалоги с противниками
        - speaker: 
          remark: 
      enemy:  # название противника, с которым игрок встретится
      amount: 

    destination:  # часть 3: доставка ресурсов
      dialogs:  # диалог с персонажем B, который ждет доставку ресурсов
        - speaker: 
          remark: 
      character_to_deliver:  # имя персонажа B

  objective_description:  # описание цели для игрока
  reward:  # награда за прохождение квеста
    item_name: 

  explanation:  # дать комментарии, почему был сгенерирован именно такой квест
Комментарии в YAML можно убрать. Диалоги в разделах dialogs могут содержать от 5 до 10 вхождений.
