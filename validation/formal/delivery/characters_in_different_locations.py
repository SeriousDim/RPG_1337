from model.objects.characters import find_character_by_name
from validation.formal.base.abstract_validation import AbstractValidation


class CharactersInDifferentLocationsValidation(AbstractValidation):
    description = "Персонажи quest.parts.resource_to_deliver.character и quest.parts.destination.character_to_deliver должны находится в разных локациях"
    
    def validate(self, quest: dict) -> bool:
        character_a_name = quest['parts']['resource_to_deliver']['character']
        character_b_name = quest['parts']['destination']['character_to_deliver']
        
        character_a = find_character_by_name(character_a_name)
        character_b = find_character_by_name(character_b_name)
        
        if character_a.location.name == character_b.location.name:
            self.raise_validation_error(
                f"Персонажи '{character_a_name}' и '{character_b_name}' находятся в одной локации '{character_a.location.name}'"
            )
        
        return True

