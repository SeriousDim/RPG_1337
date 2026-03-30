from dataclasses import dataclass

from model.player.player_armor import PlayerArmor
from prompt.model.item_dto import ItemDto


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
    
    def __dict__(self):
        return {
            "current_armor_absorbed_damage": self.current_armor_absorbed_damage,
            "max_possible_armor_absorbed_damage": self.max_possible_armor_absorbed_damage,
            "helmet": self.helmet.__dict__() if self.helmet else None,
            "chestplate": self.chestplate.__dict__() if self.chestplate else None,
            "leggings": self.leggings.__dict__() if self.leggings else None,
            "shield": self.shield.__dict__() if self.shield else None
        }
        
