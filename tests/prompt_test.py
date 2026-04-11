from experiment.single_generation import SingleQuestGeneration
from generation.const import DELIVERY, PLAYER_KEY, GAME_KEY, QUEST_TYPE_KEY, QUEST_FORMAT_KEY
from generation.context.quest_context_generator import QuestContextGenerator
from llm.langchain.create_model import create_langchain_model
from llm.langchain.model_handlers import create_gpt_model
from llm.providers import PROVIDERS
from model.game.state.game_state import GameState
from prompt.generator.prompt_generator import create_prompt
from prompt.parser.result_parser import parse_result


quest_gen = SingleQuestGeneration(
    prompt_file_name="automata_v2",
    game_state=GameState(),
    provider="proxy_api",
    model="gpt-5.4-mini",
    quest_file_name='delivery_v2',
    path_to_save='single/test'
)

quest_gen.generate()
