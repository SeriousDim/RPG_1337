from dataclasses import dataclass

from model.items.item import Item
from model.locations.locations import PrimaryLocation
from prompt.model.item_dto import ItemDto


@dataclass
class Character:
    name: str
    location: PrimaryLocation
    items_can_give_after_quest_finished: list[Item]
    items_can_be_accepted_for_delivery_or_collection: list[Item]
    
    def to_dict(self):
        return {
            'name': self.name,
            'location': self.location.to_dict(),
            'items_can_give_after_quest_finished': [ItemDto(item).to_dict() for item in self.items_can_give_after_quest_finished],
            'items_can_be_accepted_for_delivery_or_collection': [ItemDto(item).to_dict() for item in self.items_can_be_accepted_for_delivery_or_collection]
        }
