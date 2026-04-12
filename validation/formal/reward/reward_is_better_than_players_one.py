from core.find import find_any_item
from model.player.player import Player
from validation.formal.base.abstract_validation import AbstractValidation


class RewardIsBetterThanPlayersOneValidation(AbstractValidation):
    player: Player
    
    def __init__(self, player: Player):
        super().__init__()
        self.player = player
        self.description = "Предлагаемая награда (quest.reward.item_name) должна быть лучше по рангу (rank), чем предметы такого же типа (type), которые есть у игрока в данный момент в его инвентаре или в броне"
    
    def validate(self, quest: dict) -> bool:
        reward = find_any_item(quest[self.REWARD]['item_name'])
        player_items = self.player.inventory + self.player.armor.get_all_armors()
        player_items = list(filter(lambda i: i.type == reward.type, player_items))
        
        if len(player_items) == 0:
            return True
        
        max_rank = max(map(lambda i: i.rank, player_items))
        if reward.rank <= max_rank:
            self.raise_validation_error(
                f"Награда '{reward.name}' ранга {reward.rank} должна быть лучше предметов игрока того же типа. Максимальный ранг у игрока: {max_rank}"
            )
        return True

