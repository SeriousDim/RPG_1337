from model.items.resource import Resource
from model.objects.objects import find_any_item_by_name
from model.player.player import Player
from validation.formal.base.abstract_validation import AbstractValidation


class PlayerHasAppropriateInstrumentValidation(AbstractValidation):
    player: Player
    
    def __init__(self, player: Player):
        self.player = player
        self.description = "Игрок должен иметь подходящий по рангу (rank) и по типу (type) инструмент в своем инвентаре для добычи ресурса (quest.parts.resource_to_deliver.resource)"
    
    def validate(self, quest: dict) -> bool:
        resource_name = quest['parts']['resource_to_deliver']['resource']
        resource = find_any_item_by_name(resource_name)
        
        if isinstance(resource, Resource):
            min_instrument_level = resource.min_instrument_rank
            resource_type = resource.type
            
            if resource_type == 'трава':
                best_instrument_rank = self.find_best_instrument_rank(self.player.inventory, 'лопата')
                return best_instrument_rank >= min_instrument_level
            elif resource_type == 'руда':
                best_instrument_rank = self.find_best_instrument_rank(self.player.inventory, 'кирка')
                return best_instrument_rank >= min_instrument_level
            return False
        else:
            return False
    
    def find_best_instrument_rank(self, instruments, type):
        filtered_by_type = list(filter(lambda i: i.type == type, instruments))
        if len(filtered_by_type) == 0:
            return 0
        return max(map(lambda i: i.rank, filtered_by_type))
