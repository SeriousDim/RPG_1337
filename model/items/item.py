from abc import ABC
from dataclasses import dataclass


@dataclass
class Item(ABC):
    rank: int
    name: str
