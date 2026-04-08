from validation.formal.base.abstract_validation import AbstractValidation


class CharacterIsSamePlayerInteractedValidation(AbstractValidation):
    def validate(self, quest: dict) -> bool:
        
