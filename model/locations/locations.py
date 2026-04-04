from dataclasses import dataclass

from model.items.resource import Resource


@dataclass
class PrimaryLocation:
    name: str
    
    def __dict__(self):
        return {
            "name": self.name,
        }


@dataclass
class BufferedLocation:
    name: str
    herb_resource: Resource
    ore_resource: Resource
