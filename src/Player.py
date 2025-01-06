import math
class Player:
    # Originally I wanted to also set the random strength value as a standard value just like health.
    # The unittests however decided for me, so now you need to declare it in the initialization.
    def __init__(self, name, strength, health = 100):
        self._name = name
        self._health = health
        self._strength = strength
    # The following getters caused me to have a decent headache. I mean I know that they are required.
    # And I like to have them and making them isn't that much of a problem for me. But finding what the unittests
    # wanted from me is a whole different story.
    # I wish that the public / private declaration of things would be more conclusive... Like in C++....
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
        # Since I was able to make this a oneliner I made it a oneliner.
        return f'Player {self.name} has {self.strength} strength and {self.health} health.'
    # I had tried to make the tests for too low health in here and just returning a bool which could be caught
    # by an if-statement in the call. However, the unittests decided that I didn't.
    def take_damage(self, damage):
        if self._health - damage >= 0:
            self._health -= damage
        else:
            self._health = 0
    # That I had to import the math package just to round the health down, makes me furious...
    def regain_health(self, health_regained):
        if self._health + health_regained > 100:
            self._health = 100
        else:
            self._health = math.floor(health_regained + self.health)

