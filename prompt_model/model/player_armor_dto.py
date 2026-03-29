from dataclasses import dataclass

from model.items.item import Item
from model.player.player_armor import PlayerArmor
from prompt_model.model.item_dto import ItemDto


@dataclass
class PlayerArmorDto:
    current_armor_absorbed_damage: int
    max_possible_armor_absorbed_damage: int
    helmet: ItemDto
    chestplate: ItemDto
    leggings: ItemDto
    shield: ItemDto
    
    def __init__(self, armor: PlayerArmor):
        self.current_armor_absorbed_damage = armor.current_armor_absorbed_damage
        self.max_possible_armor_absorbed_damage = armor.max_possible_armor_absorbed_damage
        self.helmet = ItemDto(armor.helmet) if armor.helmet else None
        self.chestplate = ItemDto(armor.chestplate) if armor.chestplate else None
        self.leggings = ItemDto(armor.leggings) if armor.leggings else None
        self.shield = ItemDto(armor.shield) if armor.shield else None
        
