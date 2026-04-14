# results/generated/deepseek/deepseek-v3.2-automata_v2-delivery_v2/quest11
2026-04-13 22:33:47

AllQuestKeysExistValidation: ⚠️
Структура квеста соответствует заданному формату, все необходимые ключи прописаны

```
Traceback (most recent call last):
  File "C:\Projects\rpg_quest\experiment\formal_validator.py", line 199, in run_validation_list
    quest_content = quest_yaml['quest']
                    ~~~~~~~~~~^^^^^^^^^
TypeError: 'NoneType' object is not subscriptable
```

EntitiesExistenceValidation: ⚠️
Все упоминаемые сущности в структуре квеста должны существовать в игре

```
Traceback (most recent call last):
  File "C:\Projects\rpg_quest\experiment\formal_validator.py", line 199, in run_validation_list
    quest_content = quest_yaml['quest']
                    ~~~~~~~~~~^^^^^^^^^
TypeError: 'NoneType' object is not subscriptable
```

BalanceValidation: ⚠️
Игрок может пройти часть квеста, в которой он встречается с противником (quest.parts.enemy_to_face)

```
Traceback (most recent call last):
  File "C:\Projects\rpg_quest\experiment\formal_validator.py", line 199, in run_validation_list
    quest_content = quest_yaml['quest']
                    ~~~~~~~~~~^^^^^^^^^
TypeError: 'NoneType' object is not subscriptable
```

PlayerHasAppropriateInstrumentValidation: ⚠️
Игрок должен иметь подходящий по рангу (rank) и по типу (type) инструмент в своем инвентаре для добычи ресурса (quest.parts.resource_to_deliver.resource)

```
Traceback (most recent call last):
  File "C:\Projects\rpg_quest\experiment\formal_validator.py", line 199, in run_validation_list
    quest_content = quest_yaml['quest']
                    ~~~~~~~~~~^^^^^^^^^
TypeError: 'NoneType' object is not subscriptable
```

RewardIsBetterThanPlayersOneValidation: ⚠️
Предлагаемая награда (quest.reward.item_name) должна быть лучше по рангу (rank), чем предметы такого же типа (type), которые есть у игрока в данный момент в его инвентаре или в броне

```
Traceback (most recent call last):
  File "C:\Projects\rpg_quest\experiment\formal_validator.py", line 199, in run_validation_list
    quest_content = quest_yaml['quest']
                    ~~~~~~~~~~^^^^^^^^^
TypeError: 'NoneType' object is not subscriptable
```

PlayerHasNotSuchRewardValidation: ⚠️
Предлагаемая награда (quest.reward.item_name) не должна быть в наличии в инвентаре или в броне игрока

```
Traceback (most recent call last):
  File "C:\Projects\rpg_quest\experiment\formal_validator.py", line 199, in run_validation_list
    quest_content = quest_yaml['quest']
                    ~~~~~~~~~~^^^^^^^^^
TypeError: 'NoneType' object is not subscriptable
```

CharacterIsSamePlayerInteractedValidation: ⚠️
Персонаж quest.parts.resource_to_deliver.character совпадает с персонажем, к которому подошел игрок

```
Traceback (most recent call last):
  File "C:\Projects\rpg_quest\experiment\formal_validator.py", line 199, in run_validation_list
    quest_content = quest_yaml['quest']
                    ~~~~~~~~~~^^^^^^^^^
TypeError: 'NoneType' object is not subscriptable
```

CharactersInDifferentLocationsValidation: ⚠️
Персонажи quest.parts.resource_to_deliver.character и quest.parts.destination.character_to_deliver должны находится в разных локациях

```
Traceback (most recent call last):
  File "C:\Projects\rpg_quest\experiment\formal_validator.py", line 199, in run_validation_list
    quest_content = quest_yaml['quest']
                    ~~~~~~~~~~^^^^^^^^^
TypeError: 'NoneType' object is not subscriptable
```

ItemIsAcceptableByCharacterValidation: ⚠️
Предлагаемый ресурс для добычи (quest.parts.resource_to_deliver.resource) должен приниматься персонажем в quest.parts.destination.character_to_deliver

```
Traceback (most recent call last):
  File "C:\Projects\rpg_quest\experiment\formal_validator.py", line 199, in run_validation_list
    quest_content = quest_yaml['quest']
                    ~~~~~~~~~~^^^^^^^^^
TypeError: 'NoneType' object is not subscriptable
```

CharacterCanGiveRewardValidation: ⚠️
Персонаж (quest.parts.destination.character_to_deliver) действительно может давать данный предмет (quest.reward.item_name) в качестве награды

```
Traceback (most recent call last):
  File "C:\Projects\rpg_quest\experiment\formal_validator.py", line 199, in run_validation_list
    quest_content = quest_yaml['quest']
                    ~~~~~~~~~~^^^^^^^^^
TypeError: 'NoneType' object is not subscriptable
```

RemarkValidation: ⚠️
Генерируется заданный диапазон (от 5 до 10) реплик (dialogs) для каждой из частей (quest.parts)

```
Traceback (most recent call last):
  File "C:\Projects\rpg_quest\experiment\formal_validator.py", line 199, in run_validation_list
    quest_content = quest_yaml['quest']
                    ~~~~~~~~~~^^^^^^^^^
TypeError: 'NoneType' object is not subscriptable
```
