# results/generated/text_exp/quest1
2026-04-12 21:43:20

AllQuestKeysExistValidation: ✅
Структура квеста соответствует заданному формату, все необходимые ключи прописаны

EntitiesExistenceValidation: ✅
Все упоминаемые сущности в структуре квеста должны существовать в игре

BalanceValidation: ✅
Игрок может пройти часть квеста, в которой он встречается с противником (quest.parts.enemy_to_face)

PlayerHasAppropriateInstrumentValidation: ❌
Игрок должен иметь подходящий по рангу (rank) и по типу (type) инструмент в своем инвентаре для добычи ресурса (quest.parts.resource_to_deliver.resource)

```
Для добычи ресурса 'Одуванчик' нужен инструмент 'лопата' ранга не ниже 1, но у игрока лучший доступный ранг равен 0
```

RewardIsBetterThanPlayersOneValidation: ✅
Предлагаемая награда (quest.reward.item_name) должна быть лучше по рангу (rank), чем предметы такого же типа (type), которые есть у игрока в данный момент в его инвентаре или в броне

PlayerHasNotSuchRewardValidation: ✅
Предлагаемая награда (quest.reward.item_name) не должна быть в наличии в инвентаре или в броне игрока

CharacterIsSamePlayerInteractedValidation: ⚠️
Персонаж quest.parts.resource_to_deliver.character совпадает с персонажем, к которому подошел игрок

```
Traceback (most recent call last):
  File "C:\Projects\rpg_quest\experiment\formal_validator.py", line 200, in run_validation_list
    validation_result = validation.validate(quest_content)
  File "C:\Projects\rpg_quest\validation\formal\dialogs\character_is_same_player_interacted.py", line 14, in validate
    if character_name != self.interacted_character.name:
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'name'
```

CharactersInDifferentLocationsValidation: ❌
Персонажи quest.parts.resource_to_deliver.character и quest.parts.destination.character_to_deliver должны находится в разных локациях

```
Персонажи 'Гаррик Кузнец' и 'Гаррик Кузнец' находятся в одной локации 'Королевская столица'
```

ItemIsAcceptableByCharacterValidation: ✅
Предлагаемый ресурс для добычи (quest.parts.resource_to_deliver.resource) должен приниматься персонажем в quest.parts.destination.character_to_deliver

CharacterCanGiveRewardValidation: ❌
Персонаж (quest.parts.destination.character_to_deliver) действительно может давать данный предмет (quest.reward.item_name) в качестве награды

```
Персонаж 'Гаррик Кузнец' не может выдать предмет 'Железный меч' в качестве награды
```

RemarkValidation: ✅
Генерируется заданный диапазон (от 5 до 10) реплик (dialogs) для каждой из частей (quest.parts)
