"""
player:
	level:
		current_level: 
		current_xp: 
		xp_to_next_level: 
		max_possible_level: 
	statistics_for_current_session:
		enemies_killed: 
		quests_passes: 
		damage_received: 
		money_earned: 
	health:
		current: 
		max: 
	money: 
	inventory: 
		- name: Деревянный меч
		  type: оружие
		  rank: 
			  for_this_item: 1
			  max_possible_for_type: 10
		  damage_per_enemy: 
		  emenies_to_hit_per_turn: 
	armor:
		current_armor_level: 
		max_possible_armor_level: 
		helmet: empty
		chestplate:
			name: 
			rank: 
				for_this_item: 1
				max_possible: 6
			absorbed_damage: 
		leggings: empty
		shield: empty
"""

from dataclasses import dataclass

from model.items.item import Item
from model.common.health import Health
from model.player.player_armor import PlayerArmor
from model.player.player_level import PlayerLevel
from model.player.statistics import Statistics


@dataclass
class Player:
    level: PlayerLevel
    statistics_for_current_session: Statistics
    health: Health
    money: int
    inventory: list[Item]
    armor: PlayerArmor
