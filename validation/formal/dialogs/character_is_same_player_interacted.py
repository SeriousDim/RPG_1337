from model.mobs.character import Character
from validation.formal.base.abstract_validation import AbstractValidation


class CharacterIsSamePlayerInteractedValidation(AbstractValidation):
    interacted_character: Character
    
    def __init__(self, interacted_character: Character):
        self.interacted_character = interacted_character
        self.description = "Персонаж quest.parts.resource_to_deliver.character совпадает с персонажем, к которому подошел игрок"
    
    def validate(self, quest: dict) -> bool:
        character_name = quest['parts']['resource_to_deliver']['character']
        if character_name != self.interacted_character.name:
            self.raise_validation_error(
                f"Ожидался персонаж '{self.interacted_character.name}', но в quest.parts.resource_to_deliver.character указан '{character_name}'"
            )
        return True

