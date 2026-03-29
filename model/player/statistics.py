from dataclasses import dataclass


@dataclass
class Statistics:
    enemies_killed: int = 0
    quests_passes: int = 0
    damage_received: int = 0
    money_earned: int = 0
