from dataclasses import dataclass


@dataclass
class PlayerLevel:
    current_level: int
    current_xp: int
    xp_to_next_level: int
    max_possible_level: int
