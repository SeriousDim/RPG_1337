from dataclasses import dataclass

from model.items.item import Item


@dataclass
class Reward:
    item: Item


@dataclass
class Quest:
    reward: Reward
    explanation: str
