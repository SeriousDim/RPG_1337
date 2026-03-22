from dataclasses import dataclass
from model.items.item import Item


@dataclass
class Instrument(Item):
    name: str

