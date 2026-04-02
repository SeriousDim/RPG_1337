from dataclasses import dataclass

from model.game.context.armors import Armors
from model.game.context.resources import Resources
from model.items.instrument import Instrument
from model.items.weapon import Weapon


@dataclass
class Items:
    resources: Resources
    weapons: list[Weapon]
    instruments: list[Instrument]
    armor: Armors
