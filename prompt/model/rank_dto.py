from dataclasses import dataclass


@dataclass
class RankDto:
    for_this_item: int
    max_possible: int
    
    def __dict__(self):
        return {
            "for_this_item": self.for_this_item,
            "max_possible": self.max_possible
        }
