from model.items.instrument import Instrument
from model.objects.player import INITIAL_HEALTH, INITIAL_MONEY
from model.common.health import Health
from model.player.player import Player
from model.player.player_armor import PlayerArmor
from model.player.player_level import PlayerLevel
from model.player.statistics import Statistics

from model.items.sword import Sword
from model.objects.objects import PICKAXES, SHOVELS, SWORDS

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
        starter_pickaxe: Instrument = PICKAXES[0]
        starter_shovel: Instrument = SHOVELS[0]
        armor = PlayerArmor()

        return Player(
            level=level,
            statistics_for_current_session=statistics,
            health=health,
            money=INITIAL_MONEY,
            inventory=[starter_sword, starter_pickaxe, starter_shovel],
            armor=armor,
        )
        
    @staticmethod
    def create_lvl_5_player() -> Player:
        pass
    
