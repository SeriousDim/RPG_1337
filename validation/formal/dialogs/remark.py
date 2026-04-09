from validation.formal.base.abstract_validation import AbstractValidation


class RemarkValidation(AbstractValidation):
    MIN_REMARKS = 5
    MAX_REMARKS = 10
    description = f"Генерируется заданный диапазон (от {MIN_REMARKS} до {MAX_REMARKS}) реплик (dialogs) для каждой из частей (quest.parts)"
    
    def validate(self, quest: dict) -> bool:
        parts = quest['parts']
        
        for part_key in parts.keys():
            part = parts[part_key]
            dialogs = part['dialogs']
            if len(dialogs) < self.MIN_REMARKS:
                return False
            elif len(dialogs) > self.MAX_REMARKS:
                return False
        
        return True
