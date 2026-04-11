from experiment.formal_validator import FormalQuestValidator
from model.game.state.game_state import GameState


validator = FormalQuestValidator()
game_state=GameState()

validator.validate("./results/generated/text_exp", game_state.player, None)
