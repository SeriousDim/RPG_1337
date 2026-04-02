from generation.const import DELIVERY, PLAYER_KEY, GAME_KEY, QUEST_TYPE_KEY, QUEST_FORMAT_KEY
from generation.context.quest_context_generator import QuestContextGenerator
from llm.langchain.model_handlers import create_gpt_model
from llm.providers import PROVIDERS
from model.game.state.game_state import GameState
from prompt.generator.prompt_generator import create_prompt


state = GameState()

provider = PROVIDERS["proxy_api"]
prompt_template = create_prompt("automata_v1")
print("Prompt created")
llm = create_gpt_model("gpt-5.2", provider=provider)
print("LLM initialised")

chain = prompt_template
keys = [PLAYER_KEY, GAME_KEY, QUEST_TYPE_KEY, QUEST_FORMAT_KEY]
context = QuestContextGenerator.generate(keys, state, DELIVERY)
print("Filling prompt context")

result = chain.invoke(context)

with open("./results/result_prompt.md", "w", encoding='UTF-8') as f:
    f.write(result.messages[0].content)
