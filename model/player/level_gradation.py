from dataclasses import dataclass


@dataclass
class LevelGradation:
    level: int
    xp_to_next_level: int
