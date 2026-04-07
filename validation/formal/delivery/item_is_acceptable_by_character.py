from model.objects.characters import find_character_by_name
from validation.formal.base.abstract_validation import AbstractValidation


class ItemIsAcceptableByCharacterValidation(AbstractValidation):
    description = "Предлагаемый предмет для добычи должен приниматься данным персонажем в части destination"
    
    def validate(self, quest: dict) -> bool:
        part = quest['parts'][self.RESOURCE_TO_DELIVER]
        resource_name = part['resource']
        
        character_name = quest['parts'][self.DESTINATION]['character_to_deliver']
        items_to_accept = find_character_by_name(character_name).items_can_be_accepted_for_delivery_or_collection
        items_to_accept = list(map(lambda i: i.name, items_to_accept))
        
        return self.validate_name(resource_name, items_to_accept)
        
