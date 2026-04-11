# results/generated/text_exp/quest1
2026-04-12 02:06:58

AllQuestKeysExistValidation: ✅
Структура квеста соответствует заданному формату, все необходимые ключи прописаны

EntitiesExistenceValidation: ❌
Все упоминаемые сущности в структуре квеста должны существовать в игре

BalanceValidation: ⚠️
Игрок может пройти часть квеста, в которой он встречается с противником (quest.parts.enemy_to_face)

```
Traceback (most recent call last):
  File "C:\Projects\rpg_quest\experiment\formal_validator.py", line 197, in run_validation_list
    validation_result = validation.validate(quest_content)
  File "C:\Projects\rpg_quest\validation\formal\enemy\balance.py", line 36, in validate
    current_enemies = [deepcopy(enemy) for i in range(enemy_amount)]
                       ~~~~~~~~^^^^^^^
  File "C:\Users\dlyko\miniconda3\Lib\copy.py", line 163, in deepcopy
    y = _reconstruct(x, memo, *rv)
  File "C:\Users\dlyko\miniconda3\Lib\copy.py", line 260, in _reconstruct
    state = deepcopy(state, memo)
  File "C:\Users\dlyko\miniconda3\Lib\copy.py", line 137, in deepcopy
    y = copier(x, memo)
  File "C:\Users\dlyko\miniconda3\Lib\copy.py", line 222, in _deepcopy_dict
    y[deepcopy(key, memo)] = deepcopy(value, memo)
                             ~~~~~~~~^^^^^^^^^^^^^
  File "C:\Users\dlyko\miniconda3\Lib\copy.py", line 163, in deepcopy
    y = _reconstruct(x, memo, *rv)
  File "C:\Users\dlyko\miniconda3\Lib\copy.py", line 269, in _reconstruct
    y.__dict__.update(state)
    ^^^^^^^^^^^^^^^^^
AttributeError: 'function' object has no attribute 'update'
```

PlayerHasAppropriateInstrumentValidation: ⚠️
Игрок должен иметь подходящий по рангу (rank) и по типу (type) инструмент в своем инвентаре для добычи ресурса (quest.parts.resource_to_deliver.resource)

```
Traceback (most recent call last):
  File "C:\Projects\rpg_quest\experiment\formal_validator.py", line 197, in run_validation_list
    validation_result = validation.validate(quest_content)
  File "C:\Projects\rpg_quest\validation\formal\delivery\player_has_appropriate_instrument.py", line 16, in validate
    resource = find_any_item_by_name(resource_name)
  File "C:\Projects\rpg_quest\model\objects\objects.py", line 96, in find_any_item_by_name
    filtered = list(filter(lambda i: i.name == name, get_resources()))
                    ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'Resources' object is not iterable
```

RewardIsBetterThanPlayersOneValidation: ✅
Предлагаемая награда (quest.reward.item_name) должна быть лучше по рангу (rank), чем предметы такого же типа (type), которые есть у игрока в данный момент в его инвентаре или в броне

PlayerHasNotSuchRewardValidation: ✅
Предлагаемая награда (quest.reward.item_name) не должна быть в наличии в инвентаре или в броне игрока

CharactersInDifferentLocationsValidation: ❌
Персонажи quest.parts.resource_to_deliver.character и quest.parts.destination.character_to_deliver должны находится в разных локациях

ItemIsAcceptableByCharacterValidation: ✅
Предлагаемый ресурс для добычи (quest.parts.resource_to_deliver.resource) должен приниматься персонажем в quest.parts.destination.character_to_deliver

CharacterCanGiveRewardValidation: ❌
Персонаж (quest.parts.destination.character_to_deliver) действительно может давать данный предмет (quest.reward.item_name) в качестве награды

RemarkValidation: ✅
Генерируется заданный диапазон (от 5 до 10) реплик (dialogs) для каждой из частей (quest.parts)
