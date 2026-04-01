from model.player.player import Player
from prompt.model.item_dto import ItemDto
from prompt.model.player import Player as PromptPlayer
from prompt.model.player_armor_dto import PlayerArmorDto


class PlayerPromptMapper:
    
    @staticmethod
    def to(player: Player) -> PromptPlayer:
        return PromptPlayer(
            level=player.level,
            statistics_for_current_session=player.statistics_for_current_session,
            health=player.health,
            money=player.money,
            inventory=[ItemDto(item) for item in player.inventory],
            armor=PlayerArmorDto(player.armor),
        )
