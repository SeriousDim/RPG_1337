from model.player.player import Player
from validation.formal.base.abstract_validation import AbstractValidation


class PlayerHasNotSuchRewardValidation(AbstractValidation):
    player: Player
    
    def __init__(self, player: Player):
        super().__init__()
        self.player = player
        self.description = "Предлагаемая награда (quest.reward.item_name) не должна быть в наличии в инвентаре или в броне игрока"
    
    def validate(self, quest: dict) -> bool:
        reward = quest[self.REWARD]['item_name']
        player_items = self.player.inventory + self.player.armor.get_all_armors()
        player_items = [armor.name for armor in player_items]
        return reward not in player_items
