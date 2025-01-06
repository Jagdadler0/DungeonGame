class Monster:
    def __init__(self, name, strength, health):
        self._name = name
        self._strength = strength
        self._health = health
        # healthToRegain is supposed to be a constant value of the Monsters health.
        # This is to ensure that the player will receive the correct amount of health
        # after the Monster is defeated
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
    def __str__(self):
        return f'Monster {self.name} has {self.strength} strength and {self.health} health.'
    def take_damage(self, damage):
        if self._health - damage >= 0:
            self._health -= damage
            self._lost_health += damage
        else:
            self._lost_health += damage + (self._health - damage)
            self._health = 0
