import random
class Player:
    def __init__(self, name, strength = random.randint(40,80), health = 100):
        self.name = name
        self.health = health
        self.strength = strength
    def __str__(self):
        return f'Player {self.name} has {self.strength} strength and {self.health} health.'
    # The Idea behind sending a False value back if the health is below
    # 0 is to eventually call the function in an if statement and to
    # then follow up on that.
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            return False
        return True
    def regain_health(self, health_regained):
        self.health += health_regained
        if self.health > 100:
            self.health = 100
