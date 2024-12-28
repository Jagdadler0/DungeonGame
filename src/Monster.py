import random
class Monster:
    def __init__(self, name, strength = random.randint(20,40), health = random.randint(40,80)):
        self.name = name
        self.strength = strength
        self.health = health
        # healthToRegain is supposed to be a constant value of the Monsters health.
        # This is to ensure that the player will receive the correct amount of health
        # after the Monster is defeated
        self.healthToRegain = health/2
    def __str__(self):
        return f'Monster {self.name} has {self.strength} strength and {self.health} health.'
    # This is the same as for the Player. If the task stated to also improve the whole
    # thing I would have made them object-oriented with a parent class that they are
    # based upon. However since the task is not saying that I'm not doing it until
    # Milestone 'Version 2'
    # Otherwise to understand how it works/ how it's supposed to work look at Player.take_damage()
    def take_damage(self, damage):
        self.health -= damage