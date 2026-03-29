from dataclasses import dataclass

from model.items.armor import Armor


@dataclass
class PlayerArmor:
    current_armor_absorbed_damage: int = 0
    max_possible_armor_absorbed_damage: int = 0
    helmet: Armor = None
    chestplate: Armor = None
    leggings: Armor = None
    shield: Armor = None
    
    def set_helmet(self, helmet: Armor):
        self.helmet = helmet
        self._update_absorbed_damage()
    
    def set_chestplate(self, chestplate: Armor):
        self.chestplate = chestplate
        self._update_absorbed_damage()
    
    def set_leggings(self, leggings: Armor):
        self.leggings = leggings
        self._update_absorbed_damage()
    
    def set_shield(self, shield: Armor):
        self.shield = shield
        self._update_absorbed_damage()
    
    def _update_absorbed_damage(self):
        self.current_armor_absorbed_damage = 0
        self.current_armor_absorbed_damage += self.helmet.absorbed_damage
        self.current_armor_absorbed_damage += self.chestplate.absorbed_damage
        self.current_armor_absorbed_damage += self.leggings.absorbed_damage
        self.current_armor_absorbed_damage += self.shield.absorbed_damage
