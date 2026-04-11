from dataclasses import dataclass

from generation.const import PLAYER_KEY, GAME_KEY, QUEST_TYPE_KEY, QUEST_FORMAT_KEY
from generation.context.quest_context_generator import QuestContextGenerator
from llm.langchain.create_model import create_langchain_model
from llm.langchain.model_handlers import create_gpt_model
from llm.providers import PROVIDERS
from model.game.state.game_state import GameState
from prompt.generator.prompt_generator import create_prompt
from prompt.parser.result_parser import parse_result

@dataclass
class SingleQuestGeneration:
    prompt_file_name: str
    game_state: GameState
    provider: str
    model: str
    quest_file_name: str
    path_to_save: str
    
    def generate(self):
        print("Initialising game state")

        print("Creating prompt")
        provider = PROVIDERS[self.provider]
        prompt_template = create_prompt(self.prompt_file_name)

        print("Creating LLM")
        llm = create_langchain_model(self.model, provider=provider)

        chain = prompt_template | llm | parse_result
        keys = [PLAYER_KEY, GAME_KEY, QUEST_TYPE_KEY, QUEST_FORMAT_KEY]

        print("Filling prompt context")
        context = QuestContextGenerator.generate(keys, self.game_state, self.quest_file_name)

        print("Pending request")
        result = chain.invoke(context)
        result.path_to_save = self.path_to_save

        print("Saving result")
        result.save()

        print("Done")
