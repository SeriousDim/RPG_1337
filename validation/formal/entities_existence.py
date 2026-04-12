from model.objects.armors import get_armor_names
from model.objects.characters import get_character_names
from model.objects.enemies import get_enemy_names
from model.objects.objects import get_instrument_names, get_resources_names, get_swords_names
from validation.formal.base.abstract_validation import AbstractValidation


class EntitiesExistenceValidation(AbstractValidation):
    description = "Все упоминаемые сущности в структуре квеста должны существовать в игре"
    
    def validate(self, quest: dict):
        if 'parts' not in quest:
            self.raise_validation_error("В квесте отсутствует ключ 'parts'")

        parts = quest['parts']
        
        if self.RESOURCE_TO_DELIVER not in parts:
            self.raise_validation_error("В quest.parts отсутствует часть 'resource_to_deliver'")
        self.validate_resource_to_deliver_part(parts[self.RESOURCE_TO_DELIVER])
        
        if self.ENEMY_TO_FACE not in parts:
            self.raise_validation_error("В quest.parts отсутствует часть 'enemy_to_face'")
        self.validate_enemy_to_face_part(parts[self.ENEMY_TO_FACE])
        
        if self.DESTINATION not in parts:
            self.raise_validation_error("В quest.parts отсутствует часть 'destination'")
        self.validate_destination(parts[self.DESTINATION])
        
        if self.REWARD not in quest:
            self.raise_validation_error("В квесте отсутствует ключ 'reward'")
        self.validate_reward(quest[self.REWARD])
        
        return True
    
    def validate_dialogs(self, quest_part: dict, possible_characters: list) -> bool:
        dialogs = quest_part['dialogs']
        for index, dialog in enumerate(dialogs):
            self.validate_name(
                dialog['speaker'],
                possible_characters,
                f"В dialogs[{index}] указан неизвестный персонаж '{dialog['speaker']}'"
            )
        
        return True
    
    def validate_resource_to_deliver_part(self, quest_part: dict) -> bool:
        resource_names = get_resources_names()
        character_names = get_character_names()
        
        self.validate_name(
            quest_part['character'],
            character_names,
            f"Персонаж '{quest_part['character']}' в части resource_to_deliver не существует"
        )
        
        self.validate_name(
            quest_part['resource'],
            resource_names,
            f"Ресурс '{quest_part['resource']}' в части resource_to_deliver не существует"
        )
        
        return self.validate_dialogs(quest_part, character_names)
    
    def validate_enemy_to_face_part(self, quest_part: dict) -> bool:
        enemy_names = get_enemy_names()
        
        self.validate_name(
            quest_part['enemy'],
            enemy_names,
            f"Враг '{quest_part['enemy']}' в части enemy_to_face не существует"
        )
        
        return self.validate_dialogs(quest_part, enemy_names)
    
    def validate_destination(self, quest_part: dict) -> bool:
        character_names = get_character_names()
        
        self.validate_name(
            quest_part['character_to_deliver'],
            character_names,
            f"Персонаж '{quest_part['character_to_deliver']}' в части destination не существует"
        )
        
        return self.validate_dialogs(quest_part, character_names)
    
    def validate_reward(self, quest_part: dict) -> bool:
        names = get_swords_names() + get_instrument_names() + get_armor_names()
        
        self.validate_name(
            quest_part['item_name'],
            names,
            f"Награда '{quest_part['item_name']}' не существует среди доступных предметов"
        )
        
        return True

