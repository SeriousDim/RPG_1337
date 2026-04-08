from validation.formal.base.abstract_validation import AbstractValidation


class MoneyValidation(AbstractValidation):
    def validate(self, quest: dict) -> bool:
        
