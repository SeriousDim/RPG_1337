from experiment.many_generations import ManyQuestGenerations
from model.game.state.game_state import GameState

game_state=GameState()
quest_file_name='delivery_v2'
context = ManyQuestGenerations.build_context(game_state, quest_file_name)

quest_gen = ManyQuestGenerations(
    prompt_file_name="automata_v2",
    provider="proxy_api",
    context=context,
    model="gpt-5.4-mini",
    experiment_name="text_exp_2",
    amount=3
)

quest_gen.generate()
