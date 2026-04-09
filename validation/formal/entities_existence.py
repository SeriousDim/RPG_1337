from model.objects.armors import get_armor_names
from model.objects.characters import get_character_names
from model.objects.enemies import get_enemy_names
from model.objects.objects import get_instrument_names, get_resources_names, get_swords_names
from validation.formal.base.abstract_validation import AbstractValidation


class EntitiesExistenceValidation(AbstractValidation):
    description = "Все упоминаемые сущности в структуре квеста должны существовать в игре"
    
    def validate(self, quest: dict):
        parts = quest['parts']
        
        if self.RESOURCE_TO_DELIVER in parts:
            if not self.validate_resource_to_deliver_part(parts[self.RESOURCE_TO_DELIVER]):
                return False
        else:
            return False
        
        if self.ENEMY_TO_FACE in parts:
            if not self.validate_enemy_to_face_part(parts[self.ENEMY_TO_FACE]):
                return False
        else:
            return False
        
        if self.DESTINATION in parts:
            if not self.validate_destination(parts[self.DESTINATION]):
                return False
        else:
            return False
        
        if self.REWARD in quest:
            if not self.validate_reward(quest[self.REWARD]):
                return False
        else:
            return False
        
        return True
    
    def validate_dialogs(self, quest_part: dict) -> bool:
        character_names = get_character_names()
        
        dialogs = quest_part['dialogs']
        for dialog in dialogs:
            if not self.validate_name(dialog['speaker'], character_names):
                return False
        
        return True
    
    def validate_resource_to_deliver_part(self, quest_part: dict) -> bool:
        resource_names = get_resources_names()
        character_names = get_character_names()
        
        if not self.validate_name(quest_part['character'], character_names):
            return False
        
        if not self.validate_name(quest_part['resource'], resource_names):
            return False
        
        return self.validate_dialogs(quest_part)
    
    def validate_enemy_to_face_part(self, quest_part: dict) -> bool:
        enemy_names = get_enemy_names()
        
        if not self.validate_name(quest_part['enemy'], enemy_names):
            return False
        
        return self.validate_dialogs(quest_part)
    
    def validate_destination(self, quest_part: dict) -> bool:
        character_names = get_character_names()
        
        if not self.validate_name(quest_part['character_to_deliver'], character_names):
            return False
        
        return self.validate_dialogs(quest_part)
    
    def validate_reward(self, quest_part: dict) -> bool:
        names = get_swords_names() + get_instrument_names() + get_armor_names()
        
        if not self.validate_name(quest_part['item_name'], names):
            return False
        
        return True
