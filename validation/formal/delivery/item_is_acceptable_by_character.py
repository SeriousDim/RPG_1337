from model.objects.characters import find_character_by_name
from validation.formal.base.abstract_validation import AbstractValidation


class ItemIsAcceptableByCharacterValidation(AbstractValidation):
    description = "Предлагаемый ресурс для добычи (quest.parts.resource_to_deliver.resource) должен приниматься персонажем в quest.parts.destination.character_to_deliver"
    
    def validate(self, quest: dict) -> bool:
        part = quest['parts'][self.RESOURCE_TO_DELIVER]
        resource_name = part['resource']
        
        character_name = quest['parts'][self.DESTINATION]['character_to_deliver']
        items_to_accept = find_character_by_name(character_name).items_can_be_accepted_for_delivery_or_collection
        items_to_accept = list(map(lambda i: i.name, items_to_accept))
        
        self.validate_name(
            resource_name,
            items_to_accept,
            f"Персонаж '{character_name}' не принимает ресурс '{resource_name}' в качестве награды или добычи"
        )
        
        return True
        

        
