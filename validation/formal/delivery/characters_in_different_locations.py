from model.objects.characters import find_character_by_name
from validation.formal.base.abstract_validation import AbstractValidation


class CharactersInDifferentLocationsValidation(AbstractValidation):
    def validate(self, quest: dict) -> bool:
        character_a_name = quest['parts']['resource_to_deliver']['character']
        character_b_name = quest['parts']['destination']['character_to_deliver']
        
        character_a = find_character_by_name(character_a_name)
        character_b = find_character_by_name(character_b_name)
        
        return character_a.location.name != character_b.location.name
