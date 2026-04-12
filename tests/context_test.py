from generation.objects.player_generator import PlayerGenerator
from prompt.mapper.player_mapper import PlayerPromptMapper

import yaml

player = PlayerGenerator.create_initial_player()
prompt_player = PlayerPromptMapper.to(player)

yaml_string = yaml.safe_dump({"player": prompt_player.to_dict()}, allow_unicode=True)

print(yaml_string)