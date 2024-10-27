# Игра: Борьба с монстрами

from abc import ABC, abstractmethod
import random

# Шаг 1: Создаем абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуем конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука."

# Класс Monster, представляющий монстра
class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} получает {damage} урона. Осталось здоровья: {self.health}")

# Класс Fighter, представляющий бойца
class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} теперь использует {self.weapon.__class__.__name__}.")

    def attack(self, monster: Monster):
        print(self.weapon.attack())
        damage = random.randint(5, 15)  # Случайный урон от 5 до 15
        monster.take_damage(damage)

# Шаг 4: Реализация боя
def battle(fighter: Fighter, monster: Monster):
    while monster.is_alive():
        fighter.attack(monster)
        if not monster.is_alive():
            print(f"{monster.name} побежден!")
            break

# Пример работы программы
if __name__ == "__main__":
    # Создаем бойца с мечом
    fighter = Fighter("Воин", Sword())
    monster = Monster("Гоблин", 30)

    print("Боец выбирает меч.")
    battle(fighter, monster)

    # Создаем нового монстра для следующего боя
    monster = Monster("Тролль", 40)

    # Боец меняет оружие на лук
    fighter.change_weapon(Bow())
    print("Боец выбирает лук.")
    battle(fighter, monster)




