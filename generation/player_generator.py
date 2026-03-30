from model.objects.player import INITIAL_HEALTH, INITIAL_MONEY
from model.player.health import Health
from model.player.player import Player
from model.player.player_armor import PlayerArmor
from model.player.player_level import PlayerLevel
from model.player.statistics import Statistics

from model.items.sword import Sword
from model.objects.objects import SWORDS

class PlayerGenerator:

    @staticmethod
    def create_initial_player() -> Player:
        level = PlayerLevel(level=1)

        health = Health(
            current=INITIAL_HEALTH,
            max=INITIAL_HEALTH,
        )

        statistics = Statistics(
            enemies_killed=0,
            quests_passes=0,
            damage_received=0,
            money_earned=0,
        )

        starter_sword: Sword = SWORDS[0]
        armor = PlayerArmor()

        return Player(
            level=level,
            statistics_for_current_session=statistics,
            health=health,
            money=INITIAL_MONEY,
            inventory=[starter_sword],
            armor=armor,
        )
        
    
