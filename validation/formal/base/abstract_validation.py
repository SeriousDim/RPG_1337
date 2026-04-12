from abc import ABC, abstractmethod

from validation.formal.base.validation_error import QuestValidationError


class AbstractValidation(ABC):
    description: str
    RESOURCE_TO_DELIVER = 'resource_to_deliver'
    ENEMY_TO_FACE = 'enemy_to_face'
    DESTINATION = 'destination'
    
    REWARD = 'reward'
    OBJECTIVE = 'objective_description'
    EXPLANATION = 'explanation'
    
    @abstractmethod
    def validate(self, quest: dict) -> bool:
        pass
    
    def raise_validation_error(self, message: str) -> None:
        raise QuestValidationError(message)
    
    def validate_name(self, field, names, message: str | None = None) -> bool:
        if field not in names:
            if message is None:
                message = f"Значение '{field}' не найдено среди допустимых сущностей.\nДопустимые сущности: {names}"
            self.raise_validation_error(message)
        
        return True

