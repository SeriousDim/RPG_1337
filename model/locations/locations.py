from dataclasses import dataclass

from model.items.resource import Resource


@dataclass
class PrimaryLocation:
    name: str


@dataclass
class BufferedLocation:
    name: str
    resource: Resource
