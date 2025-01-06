import math
class Player:
    def __init__(self, name, strength, health = 100):
        self._name = name
        self._health = health
        self._strength = strength
    @property
    def name(self):
        return self._name
    @property
    def health(self):
        return self._health
    @property
    def strength(self):
        return self._strength
    def __str__(self):
        return f'Player {self.name} has {self.strength} strength and {self.health} health.'
    def take_damage(self, damage):
        if self._health - damage >= 0:
            self._health -= damage
        else:
            self._health = 0
    def regain_health(self, health_regained):
        if self._health + health_regained > 100:
            self._health = 100
        else:
            self._health = math.floor(health_regained + self.health)

