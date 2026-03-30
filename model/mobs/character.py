from dataclasses import dataclass

from model.items.item import Item
from model.locations.locations import PrimaryLocation


@dataclass
class Character:
    name: str
    location: PrimaryLocation
    items_can_give_after_quest_finished: list[Item]
    items_can_be_accepted_for_delivery_or_collection: list[Item]
