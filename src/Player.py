import random
class Player:
    def __init__(self, name, strength = random.randint(40,80), health = 100):
        self.name = name
        self.health: float = health
        self.strength = strength
    def __str__(self):
        return f'Player {self.name} has {self.strength} strength and {self.health} health.'
    def take_damage(self, damage):
        self.health -= damage
    def regain_health(self, health_regained):
        self.health: float = self.health + health_regained
        if self.health > 100:
            self.health = 100
