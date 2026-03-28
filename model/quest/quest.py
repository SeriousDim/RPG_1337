from abc import abstractmethod
from typing import Callable

from model.items.item import Item


class QuestPart:
    dialogs: list[str]
    
    @abstractmethod
    def is_done(self) -> bool:
        pass
    
    @abstractmethod
    def on_start(self):
        pass
    
    @abstractmethod
    def on_done(self):
        pass


class Quest:
    parts: list[QuestPart]
    reward: Item
