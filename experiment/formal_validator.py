import importlib
import os
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from core.resource_loader import ResourceLoader
from core.yaml.yaml_utils import load_yaml_file
from model.player.player import Player
from model.items.sword import Sword
from model.mobs.enemy import Enemy


class FormalQuestValidator:
    
    def __init__(self, quest_dirs: list[str]):
        self.quest_dirs = quest_dirs
        self.base_validations = [
            "validation.formal.entities_existence.EntitiesExistenceValidation",
            "validation.formal.all_quest_keys_exist.AllQuestKeysExistValidation",
            "validation.formal.enemy.balance.BalanceValidation"
        ]
    
    @staticmethod
    def find_quest_dirs(experiment_dir: str) -> list[str]:
        """
        Находит все подкаталоги с файлом content.yaml внутри experiment_dir.
        Возвращает список абсолютных путей к этим подкаталогам.
        """
        experiment_path = Path(experiment_dir)
        quest_dirs = []

        # Обход всех подкаталогов
        for root, dirs, files in os.walk(experiment_path):
            if 'content.yaml' in files:
                quest_dirs.append(str(Path(root).resolve()))

        return quest_dirs
    
    def validate(self):
        pass
