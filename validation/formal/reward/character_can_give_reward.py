from model.objects.characters import find_character_by_name
from validation.formal.base.abstract_validation import AbstractValidation


class CharacterCanGiveRewardValidation(AbstractValidation):
    description = "Персонаж (quest.parts.destination.character_to_deliver) действительно может давать данный предмет (quest.reward.item_name) в качестве награды"
    
    def validate(self, quest: dict):
        part = quest['parts'][self.DESTINATION]
        character_name = part['character_to_deliver']
        
        reward_name = quest[self.REWARD]['item_name']
        
        character_items = find_character_by_name(character_name).items_can_give_after_quest_finished
        character_items = [item.name for item in character_items]
        
        if reward_name not in character_items:
            self.raise_validation_error(
                f"Персонаж '{character_name}' не может выдать предмет '{reward_name}' в качестве награды"
            )
        
        return True

