from dataclasses import dataclass


@dataclass
class Statistics:
    enemies_killed: int
    quests_passes: int
    damage_received: int
    money_earned: int
