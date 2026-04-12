from dataclasses import dataclass

from model.locations.locations import PrimaryLocation, BufferedLocation as OriginalBufferedLocation
from prompt.model.item_dto import ItemDto


@dataclass
class BufferedLocation:
    name: str
    herb_resource: ItemDto
    ore_resource: ItemDto
    
    def __init__(self, location: OriginalBufferedLocation):
        self.name = location.name
        self.herb_resource = ItemDto(location.herb_resource)
        self.ore_resource = ItemDto(location.ore_resource)
    
    def to_dict(self):
        return {
            "name": self.name,
            "herb_resource": self.herb_resource.to_dict(),
            "ore_resource": self.ore_resource.to_dict()
            }


@dataclass
class Locations:
    primary: list[PrimaryLocation]
    buffered: list[BufferedLocation]
    
    def __init__(self, locations):
        self.primary = locations.primary
        self.buffered = [BufferedLocation(loc) for loc in locations.buffered]
    
    def to_dict(self):
        return {
            "primary": [loc.to_dict() for loc in self.primary],
            "buffered": [loc.to_dict() for loc in self.buffered]
        }