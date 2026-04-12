from dataclasses import dataclass


@dataclass
class RankDto:
    for_this_item: int
    max_possible: int
    
    def to_dict(self):
        return {
            "for_this_item": self.for_this_item,
            "max_possible": self.max_possible
        }
