from experiment.formal_validator import FormalQuestValidator
from model.game.state.game_state import GameState


validator = FormalQuestValidator()
game_state=GameState()

validator.validate("./results/generated/gpt-5.2-automata_v1-delivery_v2", game_state.player, None)
