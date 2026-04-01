from model.game import game_context
from model.game.context.game_objects import GameObjects
from model.game.context.items import Items
from model.mobs.character import Character
from model.objects.armors import get_armors
from model.objects.enemies import ENEMIES
from model.objects.locations import get_locations
from model.objects.objects import SWORDS, get_instruments, get_resources


class GameObjectsGenerator:
    
    @staticmethod
    def create_game_context() -> GameObjects:
        return GameObjects(
            "фентэзийное средневековье",
            items=Items(
                armor=get_armors(),
                instruments=get_instruments(),
                weapons=SWORDS,
                resources=get_resources()
            ),
            enemies=ENEMIES,
            locations=get_locations(),
            characters=[]
        )
        
