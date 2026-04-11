from dataclasses import dataclass
import os
import re
from typing import Any

from generation.context.quest_context_generator import QuestContextGenerator
from llm.langchain.create_model import create_langchain_model
from llm.providers import PROVIDERS
from model.game.state.game_state import GameState
from prompt.generator.prompt_generator import create_prompt
from prompt.parser.result import LlmResult
from prompt.parser.result_parser import parse_result
from generation.const import PLAYER_KEY, GAME_KEY, QUEST_TYPE_KEY, QUEST_FORMAT_KEY


@dataclass
class ManyQuestGenerations:
    prompt_file_name: str
    context: dict
    provider: str
    model: Any
    experiment_name: str
    amount: int
    root_path: str = "./results/generated"
    
    def __init__(self, **kwargs):
        print("Initialising experiment...\n")
        self.prompt_file_name = kwargs.get('prompt_file_name')
        self.provider = PROVIDERS[kwargs.get('provider')]
        self.context = kwargs.get('context')
        self.model = create_langchain_model(kwargs.get('model'), provider=self.provider)
        self.experiment_name = kwargs.get('experiment_name')
        self.amount = kwargs.get('amount')
        self.root_path = kwargs.get('root_path', self.root_path)
    
    @staticmethod
    def build_context(game_state: GameState, quest_file_name: str) -> dict:
        keys = [PLAYER_KEY, GAME_KEY, QUEST_TYPE_KEY, QUEST_FORMAT_KEY]
        return QuestContextGenerator.generate(keys, game_state, quest_file_name)
    
    def generate(self):
        print(f"Processing generation: {self.experiment_name}\n")
        
        full_dir_path = f"{self.root_path}/{self.experiment_name}"
        start_index = self.find_max_quest_folder(full_dir_path)
        end_index = start_index + self.amount
        for i in range(start_index, end_index):
            print(f"Generating quest {i + 1}/{end_index}")
            prompt_template = create_prompt(self.prompt_file_name)

            chain = prompt_template | self.model | parse_result
            
            result: LlmResult = chain.invoke(self.context)
            result.path_to_save = f"{self.experiment_name}/quest{i + 1}"

            print(f"Saving to {result.path_to_save}\n")
            result.save()
    
    def find_max_quest_folder(self, directory):
        max_i = 0
        
        if not os.path.exists(directory):
            print(f"Директория не найдена: {directory}")
            return 0
        
        pattern = re.compile(r'^quest(\d+)$')
        
        for item in os.listdir(directory):
            match = pattern.match(item)
            if match:
                i = int(match.group(1))
                if i > max_i:
                    max_i = i
        
        return max_i
