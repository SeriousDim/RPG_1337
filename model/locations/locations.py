from dataclasses import dataclass

from model.items.resource import Resource


@dataclass
class PrimaryLocation:
    name: str


@dataclass
class BufferedLocation:
    name: str
    herb_resource: Resource
    ore_resource: Resource
