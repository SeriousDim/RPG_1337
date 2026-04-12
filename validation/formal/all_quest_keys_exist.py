from validation.formal.base.abstract_validation import AbstractValidation


class AllQuestKeysExistValidation(AbstractValidation):
    description = "Структура квеста соответствует заданному формату, все необходимые ключи прописаны"
    
    def validate(self, quest: dict) -> bool:
        if 'parts' not in quest:
            self.raise_validation_error("В квесте отсутствует ключ 'parts'")

        missing_top_level_keys = [key for key in [self.REWARD, self.OBJECTIVE, self.EXPLANATION] if key not in quest]
        if missing_top_level_keys:
            self.raise_validation_error(
                f"В квесте отсутствуют обязательные ключи: {', '.join(missing_top_level_keys)}"
            )

        if 'item_name' not in quest['reward']:
            self.raise_validation_error("В reward отсутствует ключ 'item_name'")

        parts = quest['parts']
        missing_top_level_keys = [key for key in [self.RESOURCE_TO_DELIVER, self.ENEMY_TO_FACE, self.DESTINATION] if key not in parts]
        if missing_top_level_keys:
            self.raise_validation_error(
                f"В квесте отсутствуют обязательные ключи: {', '.join(missing_top_level_keys)}"
            )
        
        self.validate_resource_to_deliver_part(parts[self.RESOURCE_TO_DELIVER])
        self.validate_enemy_to_face_part(parts[self.ENEMY_TO_FACE])
        self.validate_destination(parts[self.DESTINATION])
        return True
    
    def validate_dialogs(self, dialogs: dict) -> bool:
        for index, dialog in enumerate(dialogs):
            if 'speaker' not in dialog or 'remark' not in dialog:
                self.raise_validation_error(
                    f"В dialogs[{index}] должны присутствовать ключи 'speaker' и 'remark'"
                )
        return True
    
    def validate_resource_to_deliver_part(self, part: dict) -> bool:
        keys = set(part.keys())
        correct_keys = {'dialogs', 'resource', 'amount', 'character'}
        
        if keys != correct_keys:
            self.raise_validation_error(
                f"В части resource_to_deliver ожидаются ключи {sorted(correct_keys)}, получены {sorted(keys)}"
            )
        
        return self.validate_dialogs(part['dialogs'])
    
    def validate_enemy_to_face_part(self, part: dict) -> bool:
        keys = set(part.keys())
        correct_keys = {'dialogs', 'enemy', 'amount'}
        
        if keys != correct_keys:
            self.raise_validation_error(
                f"В части enemy_to_face ожидаются ключи {sorted(correct_keys)}, получены {sorted(keys)}"
            )
        
        return self.validate_dialogs(part['dialogs'])
    
    def validate_destination(self, part: dict) -> bool:
        keys = set(part.keys())
        correct_keys = {'dialogs', 'character_to_deliver'}
        
        if keys != correct_keys:
            self.raise_validation_error(
                f"В части destination ожидаются ключи {sorted(correct_keys)}, получены {sorted(keys)}"
            )
        
        return self.validate_dialogs(part['dialogs'])
                

                
