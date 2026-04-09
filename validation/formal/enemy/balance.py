from model.objects.enemies import find_enemy_by_name
from model.player.player import Player
from model.items.sword import Sword
from model.mobs.enemy import Enemy
from validation.formal.base.abstract_validation import AbstractValidation
from copy import deepcopy


class BalanceValidation(AbstractValidation):
    player: Player
    
    def __init__(self, player: Player):
        self.player = player
        self.description = "Игрок может пройти часть квеста, в которой он встречается с противником (quest.parts.enemy_to_face)"
    
    def validate(self, quest: dict) -> bool:
        enemy_name = quest['parts']['enemy_to_face']['enemy']
        enemy_amount = quest['parts']['enemy_to_face']['amount']
        enemy = find_enemy_by_name(enemy_name)
        
        if enemy_amount <= 0:
            return False

        # Находим лучший меч игрока по рангу
        best_sword = None
        for item in self.player.inventory:
            if isinstance(item, Sword):
                if best_sword is None or item.rank > best_sword.rank:
                    best_sword = item

        if best_sword is None:
            # Если меча нет, игрок не может победить врагов
            return False

        # Создаем копии врагов, чтобы не изменять оригинальные объекты
        current_enemies = [deepcopy(enemy) for i in range(enemy_amount)]

        # Стратегия атаки: атакуем врагов в порядке убывания их урона (сначала самых опасных)
        # Это минимизирует урон по игроку в следующих ходах
        def enemy_attack_key(e: Enemy):
            return (e.damage_per_turn, - e.health.current)

        total_money_earned = 0

        while self.player.health.current > 0 and len(current_enemies) > 0:
            # Фаза 1: Атака игрока
            current_enemies.sort(key=enemy_attack_key, reverse=True)  # Сортируем по урону (сначала сильные)

            # Определяем, сколько врагов может ударить меч
            enemies_to_hit = min(best_sword.enemies_to_hit, len(current_enemies))
            damage_per_enemy = best_sword.damage_per_enemy

            # Если enemies_to_hit >= len(current_enemies), применяем особую логику
            if best_sword.enemies_to_hit >= len(current_enemies):
                # Наносим базовый урон всем врагам
                for enemy in current_enemies:
                    enemy.health.current -= damage_per_enemy

                # Рассчитываем остаточный урон
                left_damage = damage_per_enemy * (best_sword.enemies_to_hit - len(current_enemies))
                if len(current_enemies) > 0:
                    appliable_damage = left_damage // len(current_enemies)  # ceil(left_damage / n)
                    for enemy in current_enemies:
                        enemy.health.current -= appliable_damage
            else:
                # Наносим урон первым enemies_to_hit врагам
                for i in range(enemies_to_hit):
                    current_enemies[i].health.current -= damage_per_enemy

            # Удаляем убитых врагов и начисляем деньги
            alive_enemies = []
            for enemy in current_enemies:
                if enemy.health.current <= 0:
                    total_money_earned += enemy.money_for_killing_this_enemy
                else:
                    alive_enemies.append(enemy)
            current_enemies = alive_enemies

            # Проверяем, остались ли враги
            if len(current_enemies) == 0:
                break

            # Фаза 2: Атака врагов
            total_enemy_damage = sum(enemy.damage_per_turn for enemy in current_enemies)
            # Броня поглощает часть урона
            absorbed = self.player.armor.current_armor_absorbed_damage
            total_enemy_damage -= absorbed
            total_enemy_damage = max(0, total_enemy_damage)

            self.player.health.current -= total_enemy_damage

            # Проверяем, жив ли игрок
            if self.player.health.current <= 0:
                return False

        # Если мы дошли до сюда, значит игрок победил
        return True
