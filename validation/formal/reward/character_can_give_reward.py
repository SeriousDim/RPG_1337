from model.objects.characters import find_character_by_name
from validation.formal.base.abstract_validation import AbstractValidation


class CharacterCanGiveRewardValidation(AbstractValidation):
    description = "Данный персонаж действительно может давать данный предмет в качестве награды"
    
    def validate(self, quest: dict):
        part = quest[self.DESTINATION]
        character = part['character_to_deliver']
        
        reward_name = quest[self.REWARD].name
        
        character_items = find_character_by_name(character.name).items_can_be_accepted_for_delivery_or_collection
        character_items = [item.name for item in character_items]
        
        return reward_name in character_items
