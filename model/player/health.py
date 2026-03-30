from dataclasses import dataclass


@dataclass
class Health:
    current: int
    max: int
    
    def __dict__(self):
        return {
            "current": self.current,
            "max": self.max
        }
