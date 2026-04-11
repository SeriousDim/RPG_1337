from core.yaml.yaml_utils import _surround_with_yaml_block
from generation.const import DELIVERY
from core.resource_loader import ResourceLoader


class QuestTypeMapper:
    
    QUEST_YAMLS_PATH = 'quest_yamls'
    
    QUEST_NAMES = {
        DELIVERY: 'Доставка'
    }
    
    @staticmethod
    def handle_quest_type_key(quest_type: str) -> str:
        for key in QuestTypeMapper.QUEST_NAMES:
            if quest_type.startswith(key):
                return QuestTypeMapper.QUEST_NAMES[key]
    
    @staticmethod
    @_surround_with_yaml_block
    def handle_quest_format_key(quest_type: str) -> str:
        return ResourceLoader.load_text(f"{QuestTypeMapper.QUEST_YAMLS_PATH}/{quest_type}.yaml")
