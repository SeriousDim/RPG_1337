from dataclasses import dataclass


@dataclass
class Health:
    current: int
    max: int
    
    def to_dict(self):
        return {
            "current": self.current,
            "max": self.max
        }
