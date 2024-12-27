import Monster
import Player
import re
class Room:
    def __init__(self, description, monster: Monster.Monster):
        self.description = description
        self.monster = monster
    def __str__(self):
        return f'{self.description}'
    def fight_round(self, player: Player.Player):
        print(f'The monster hits you with {self.monster.strength} strength.')
        if not player.take_damage(self.monster.strength):
            print('You lost the fight')
            return 1
        print(player)

        print(f'You hit the monster with {player.strength} strength.')
        if not self.monster.take_damage(player.strength):
            print('The monster is dead')
            player.regain_health(self.monster.healthToRegain)
            return 2
        print(self.monster)
    def interact(self, player: Player.Player):
        print(f'Welcome to the {self.description}\nThe monster {self.monster.name} appears!')
        inp = ''
        while True:
            # Since python is python and python is no fun, I had to exchange a
            # do-while loop with this abomination.
            # I mean... it works... and it does the stuff it's supposed to but
            # I still want my do-while loops to separate
            # the input and the actual game behaviour >:[
            # In the end RegEx came to make it bearable and to only test for f and r
            inp = input('Would you like to run (r) or fight (f)\n')
            if re.search('^f',inp):
                print('You chose FIGHT!')
                val = self.fight_round(player)
                if val == 1:    # Monster is defeated
                    return # TODO Next Room must be loaded
                elif val == 2:  # Player is defeated
                    return # TODO Gameplay Loop must be ended
            elif re.search('^r',inp):
                print('You chose RUN!\nYou sprint out of the room and take 10 damage!')
                player.take_damage(10)
                break
            else:
                print('Not a valid input')
