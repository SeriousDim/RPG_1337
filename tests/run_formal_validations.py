from experiment.formal_validator import FormalQuestValidator
from model.game.state.game_state import GameState


validator = FormalQuestValidator()
game_state=GameState()

validator.validate("./results/generated/gemini-3-flash-preview-automata_v2-delivery_v2", game_state.player, None)
