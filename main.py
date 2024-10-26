# Игра: Борьба с монстрами

from abc import ABC, abstractmethod
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass
class Sword(Weapon):
    def attack(self, sword):
        print('Боец наносит удар мечом')
class Bow(Weapon):
    def attack(self, bow):
        print('Боец стреляет из лука')
class Spear(Weapon):
    def attack(self, spear):
        print('Боец бросает копье')
class Fighter():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon
    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print('Боец меняет оружие')
    def fight(self):
        print(self.weapon.attack(self.weapon))

class Monster():
    def __int__(self):
        pass

sword1 = Sword()
bow1 = Bow()
spear1 = Spear()

fighter = Fighter(sword1)
fighter.fight()

fighter = Fighter(spear1)
fighter.fight()

fighter = Fighter(bow1)
fighter.fight()

fighter.change_weapon(sword1)
fighter.fight()

fighter.change_weapon(spear1)
fighter.fight()