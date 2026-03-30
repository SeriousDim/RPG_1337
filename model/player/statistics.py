from dataclasses import dataclass


@dataclass
class Statistics:
    enemies_killed: int = 0
    quests_passes: int = 0
    damage_received: int = 0
    money_earned: int = 0
    
    def __dict__(self):
        return {
            "enemies_killed": self.enemies_killed,
            "quests_passes": self.quests_passes,
            "damage_received": self.damage_received,
            "money_earned": self.money_earned
        }
