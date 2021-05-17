from weapon import Weapon
from dinosaur import Dinosaur


class Robot:
    def __init__(self, name, health, power_level, robot_weapon):
        self.name = name
        self.health = health
        self.power_level = power_level
        self.weapon = robot_weapon

    def attack(self, name):
        if self.health > 0:
            print(self.name + ' is attacking!')
            import dinosaur
            dinosaur.health -= 10
            print(dinosaur.name + " has" + dinosaur.health + " left!")