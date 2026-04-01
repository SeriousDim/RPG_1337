from generation.const import DELIVERY
from core.resource_loader import ResourceLoader


class QuestTypeMapper:
    
    QUEST_YAMLS_PATH = 'quest_yamls'
    
    QUEST_NAMES = {
        DELIVERY: 'Доставка'
    }
    
    @staticmethod
    def handle_quest_type_key(quest_type: str) -> str:
        return QuestTypeMapper.QUEST_NAMES[quest_type]
    
    @staticmethod
    def handle_quest_format_key(quest_type: str) -> str:
        return ResourceLoader.load_text(quest_type + ".yaml")
