from dataclasses import dataclass

from model.items.instrument import Instrument


@dataclass
class Weapon(Instrument):
    def __post_init__(self):
        self.type = "оружие"
