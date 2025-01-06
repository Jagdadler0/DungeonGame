import Monster
import Player
import re
class Room:
    # The description attributes could have been private, but I'm not sure
    # if that would work with the unittests.
    def __init__(self, description, monster: Monster.Monster):
        self.description = description
        self.monster = monster
    def __str__(self):
        return f'{self.description}'
    # This just seems like bad game design to only choose between fight and flight.
    # On another note: The Pokémon (Pycharm wanted to write the "Correct" way, but we all know that it's just Pokemon)
    # games are not really better at it... If you think about it, it's just a hole lot of sprites with different numbers
    # where you choose an option, then choose a sub option and voilà a few stats change.
    # Anyways this could probably be made a bit more interesting. Even in the terminal
    def fight_round(self, player: Player.Player):
        print(f'The monster hits you with {self.monster.strength} strength.')
        player.take_damage(self.monster.strength)
        if player.health <= 0:
            print('You lost the fight')
            # I chose to make the responses for the defeat outcomes with just returning values of nothing, 1 or 2
            # since I had to do the evaluation in here. Then needed to pass it on to the calling function where I had to
            # evaluate it again... I'm just happy I didn't have to do it in the DungeonMaster.py file especially with
            # the print_results function. Oh god that would have been annoying
            return 1
        print(player)

        print(f'You hit the monster with {player.strength} strength.')
        self.monster.take_damage(player.strength)
        if self.monster.health <= 0:
            print('The monster is dead')
            # This still makes me angry. YOU KNOW WHAT HEALTH THE MONSTER HAD IN THE BEGINNING, SO WHY WOULD YOU COUNT
            # THE RECEIVED DAMAGE?! YOU CAN CALCULATE THE RECEIVED DAMAGE WITH
            # monster.original_health - monster.current_health
            # BUT OH NO IT JUST HAD TO BE THAT WAY.
            player.regain_health(self.monster.lost_health/2)
            return 2
        print(self.monster)
    def interact(self, player: Player.Player):
        print(f'Welcome to the {self.description}\nThe monster {self.monster.name} appears!')
        inp = ''
        while True:
            # And here we have a simulated do-while loop to check if something was done ONCE.
            # Thank you, Python...
            # This reminds me: Python didn't have switch-statements until Python 3.10
            # Oh also funny side note: Python is technically older then Java
            inp = input('Would you like to run (r) or fight (f)\n')
            # Oh, this is also interesting: here I used regEx to find f or r.
            # As long as you start with either r or f the following works. Which means you could write
            # 'fight', 'f', 'financial reports' or whatever you want and you still fight.
            # This leaves a way too big freedom of writing what you want but since there are not many
            # different options other than r or f it could be ignored.
            # There is still a problem of white spaces where if you input something like ' f' it wouldn't work.
            # But I can't be bothered to deal with that since it's not a required fix. (Hip, hip,
            # hooray for technicalities!)
            if re.search('^f',inp):
                print('You chose FIGHT!')
                val = self.fight_round(player)
                if val == 1:    # Monster is defeated
                    return True
                elif val == 2:  # Player is defeated
                    return False
            elif re.search('^r',inp):
                print('You chose RUN!\nYou sprint out of the room and take 10 damage!')
                player.take_damage(10)
                return True
            else:
                print('Not a valid input')

