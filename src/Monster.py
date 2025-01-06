class Monster:
    def __init__(self, name, strength, health):
        self._name = name
        self._strength = strength
        self._health = health
        # Instead of lost_health I originally just had a constant copy of the original health
        # This just made it more annoying to deal with it.
        self._lost_health = 0
    @property
    def name(self):
        return self._name
    @property
    def health(self):
        return self._health
    @property
    def strength(self):
        return self._strength
    @property
    def lost_health(self):
        return self._lost_health
    # Already said something about oneliners in Player.py
    def __str__(self):
        return f'Monster {self.name} has {self.strength} strength and {self.health} health.'
    # See comment for lost_health as to why I hate this function so much.
    # It could have been so simple...
    # Just return a false value if health reached <= 0 and call for the monsters original health.
    # And Boom! you got the exact value you want. But oh no the unittests said no. So now I had to
    # do it like this.
    # I made it work. But it could have been so much simpler.
    def take_damage(self, damage):
        if self._health - damage >= 0:
            self._health -= damage
            self._lost_health += damage
        else:
            self._lost_health += damage + (self._health - damage)
            self._health = 0
