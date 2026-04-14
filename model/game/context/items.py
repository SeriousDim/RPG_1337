from dataclasses import dataclass

from model.game.context.armors import Armors
from model.game.context.resources import Resources
from model.items.instrument import Instrument
from model.items.weapon import Weapon
from model.objects.objects import INSTRUMENT_MAPPING


@dataclass
class Items:
    resources: Resources
    weapons: list[Weapon]
    instruments: list[Instrument]
    armor: Armors
    instrument_mapping = INSTRUMENT_MAPPING
    
    def to_dict(self):
        return {
            "resources": self.resources,
            "weapons": self.weapons,
            "instruments": self.instruments,
            "armor": self.armor,
            "instrument_mapping": self.instrument_mapping
        }
