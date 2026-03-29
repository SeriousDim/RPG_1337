from dataclasses import dataclass


@dataclass
class RankDto:
    for_this_item: int
    max_possible: int
