from validation.formal.base.abstract_validation import AbstractValidation


class AllQuestKeysExistValidation(AbstractValidation):
    description = "Структура квеста соответствует заданному формату, все необходимые ключи прописаны"
    
    def validate(self, quest: dict) -> bool:
        if 'parts' not in quest:
            return False
        
        parts = quest['parts']
        return self.RESOURCE_TO_DELIVER in parts and \
                self.ENEMY_TO_FACE in parts and \
                self.DESTINATION in parts and \
                self.REWARD in quest and \
                self.OBJECTIVE in quest and \
                self.EXPLANATION in quest and \
                'item_name' in quest['reward'] and \
                self.validate_resource_to_deliver_part(parts[self.RESOURCE_TO_DELIVER]) and \
                self.validate_enemy_to_face_part(parts[self.ENEMY_TO_FACE]) and \
                self.validate_destination(parts[self.DESTINATION])
    
    def validate_dialogs(self, dialogs: dict) -> bool:
        return all(map(lambda d: 'speaker' in d and 'remark' in d, dialogs))
    
    def validate_resource_to_deliver_part(self, part: dict) -> bool:
        keys = set(part.keys())
        correct_keys = set(['dialogs', 'resource', 'amount', 'character'])
        
        if keys != correct_keys:
            return False
        
        return self.validate_dialogs(part['dialogs'])
    
    def validate_enemy_to_face_part(self, part: dict) -> bool:
        keys = set(part.keys())
        correct_keys = set(['dialogs', 'enemy', 'amount'])
        
        if keys != correct_keys:
            return False
        
        return self.validate_dialogs(part['dialogs'])
    
    def validate_destination(self, part: dict) -> bool:
        keys = set(part.keys())
        correct_keys = set(['dialogs', 'character_to_deliver'])
        
        if keys != correct_keys:
            return False
        
        return self.validate_dialogs(part['dialogs'])
                
