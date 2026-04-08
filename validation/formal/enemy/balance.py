from model.player.player import Player
from validation.formal.base.abstract_validation import AbstractValidation


class BalanceValidation(AbstractValidation):
    player: Player
    
    def __init__(self, player: Player):
        self.player = player
        self.description = "При текущем количестве здоровья, лучшем оружии и текущей броне игрок сможет одолеть данного врага в таком количестве"
    
    def validate(self, quest: dict) -> bool:
        
