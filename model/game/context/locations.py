from dataclasses import dataclass

from model.locations.locations import BufferedLocation, PrimaryLocation


@dataclass
class Locations:
    primary: list[PrimaryLocation]
    buffered: list[BufferedLocation]
