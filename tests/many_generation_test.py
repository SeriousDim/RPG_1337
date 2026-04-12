from experiment.many_generations import ManyQuestGenerations
from model.game.state.game_state import GameState

game_state=GameState()
QUEST_TYPE = 'delivery_v2'
context = ManyQuestGenerations.build_context(game_state, QUEST_TYPE)

MODEL = 'claude-haiku-4-5'
PROMPT = 'automata_v2'
quest_gen = ManyQuestGenerations(
    prompt_file_name=PROMPT,
    provider="proxy_api",
    context=context,
    model=MODEL,
    experiment_name=f"{MODEL}-{PROMPT}-{QUEST_TYPE}",
    amount=15
)

quest_gen.generate()
