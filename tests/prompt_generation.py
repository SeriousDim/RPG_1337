from experiment.many_generations import ManyQuestGenerations
from model.game.state.game_state import GameState
from prompt.generator.prompt_generator import create_prompt


game_state=GameState()
QUEST_TYPE = 'delivery_v2'
context = ManyQuestGenerations.build_context(game_state, QUEST_TYPE)
prompt_file_name = 'automata_v2'

prompt_template = create_prompt(prompt_file_name)
chain = prompt_template
result = chain.invoke(context)

with open(f"./results/prompts/{prompt_file_name}_{QUEST_TYPE}.txt", "w", encoding="utf-8") as f:
    f.write(result.messages[0].content)
