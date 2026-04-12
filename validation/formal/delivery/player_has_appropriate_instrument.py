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
        
        if not isinstance(resource, Resource):
            self.raise_validation_error(f"Ресурс '{resource_name}' не найден в каталоге ресурсов")

        min_instrument_level = resource.min_instrument_rank
        resource_type = resource.type
        
        if resource_type == 'трава':
            required_instrument = 'лопата'
        elif resource_type == 'руда':
            required_instrument = 'кирка'
        else:
            self.raise_validation_error(
                f"Для ресурса '{resource_name}' указан неподдерживаемый тип '{resource_type}'"
            )

        best_instrument_rank = self.find_best_instrument_rank(self.player.inventory, required_instrument)
        if best_instrument_rank < min_instrument_level:
            self.raise_validation_error(
                f"Для добычи ресурса '{resource_name}' нужен инструмент '{required_instrument}' ранга не ниже {min_instrument_level}, "
                f"но у игрока лучший доступный ранг равен {best_instrument_rank}"
            )
        
        return True
    
    def find_best_instrument_rank(self, instruments, type):
        filtered_by_type = list(filter(lambda i: i.type == type, instruments))
        if len(filtered_by_type) == 0:
            return 0
        return max(map(lambda i: i.rank, filtered_by_type))

