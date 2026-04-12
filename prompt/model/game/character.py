from dataclasses import dataclass

from model.locations.locations import PrimaryLocation
from prompt.model.item_dto import ItemDto


@dataclass
class Character:
    name: str
    location: PrimaryLocation
    items_can_give_after_quest_finished: list[ItemDto]
    items_can_be_accepted_for_delivery_or_collection: list[ItemDto]
    
    def __init__(self, character):
        self.name = character.name
        self.location = character.location
        self.items_can_give_after_quest_finished = [ItemDto(item) for item in character.items_can_give_after_quest_finished]
        self.items_can_be_accepted_for_delivery_or_collection = [ItemDto(item) for item in character.items_can_be_accepted_for_delivery_or_collection]
    
    def to_dict(self):
        return {
            'name': self.name,
            'location': self.location.to_dict(),
            'items_can_give_after_quest_finished': [item.to_dict() for item in self.items_can_give_after_quest_finished],
            'items_can_be_accepted_for_delivery_or_collection': [item.to_dict() for item in self.items_can_be_accepted_for_delivery_or_collection]
        }