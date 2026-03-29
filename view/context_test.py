from dataclasses import asdict

from core.yaml_utils import to_yaml_string
from generation.player_generator import PlayerGenerator
import yaml


player = PlayerGenerator.create_initial_player()

yaml_string = to_yaml_string(player, "player")

print(yaml_string)