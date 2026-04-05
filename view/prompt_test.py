from generation.const import DELIVERY, PLAYER_KEY, GAME_KEY, QUEST_TYPE_KEY, QUEST_FORMAT_KEY
from generation.context.quest_context_generator import QuestContextGenerator
from llm.langchain.create_model import create_langchain_model
from llm.langchain.model_handlers import create_gpt_model
from llm.providers import PROVIDERS
from model.game.state.game_state import GameState
from prompt.generator.prompt_generator import create_prompt
from prompt.parser.result_parser import parse_result


print("Initialising game state")
state = GameState()

print("Creating prompt")
provider = PROVIDERS["proxy_api"]
prompt_template = create_prompt("automata_v1")

print("Creating LLM")
llm = create_langchain_model("gpt-5.4-mini", provider=provider)

chain = prompt_template | llm | parse_result
keys = [PLAYER_KEY, GAME_KEY, QUEST_TYPE_KEY, QUEST_FORMAT_KEY]

print("Filling prompt context")
context = QuestContextGenerator.generate(keys, state, DELIVERY)

print("Pending request")
result = chain.invoke(context)

print("Saving result")
result.save()

print("Done")
