from abc import ABC, abstractmethod


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
    
    def validate_name(self, field, names) -> bool:
        if field not in names:
            return False
        
        return True
