import Player
import Monster
import Room
import random
# The here contained comments might not necessarily a good way of doing them.
# But oh well! Most of the stuff here isn't necessarily the way I would have done it!
# Thank you, unittests.
def __main__():
    # The amount of round could also have been an input but setting some constants is also be fine I guess
    run_game(5)
def initialize_player(username):
    return Player.Player(username, random.randint(40,80), 100)
# I quite like the way the rooms are being declared.
def initialize_rooms(rooms):
    ret_room = []
    for room in rooms:
        # I made a separate monster for each room since it A) was very long and B) I got some error? I dunno I wrote
        # this specific comment way later.
        monster = Monster.Monster(rooms[room]['monster'], random.randint(20,40), random.randint(40,80))
        ret_room.append(Room.Room(rooms[room]['desc'],monster))
    return ret_room
# I was very scared when I read the requirement for a result printer, since I thought I needed to give EVERY STRING over
# to it. But luckily it was way simpler. This could have taken hours of my live. Maybe 15 minutes of which would be
# actual work on refactoring the other functions and being done. And the majority of the time would be screaming at the
# top of my lungs about why I needed to refactor print calls.
def print_results(player):
    print('---------------------------------------------')
    print('The game is over!')
    print(player)
    print('Thank you for playing Dungeon Master!')
    print('Good Bye!')
# Dunno what to say about this. https://www.youtube.com/watch?v=YPN0qhSyWy8.
def run_game(nr_of_rooms: int):
    print('Welcome to the Dungeon')
    player = initialize_player(input('Username:\n'))
    room_config = dict()
    for i in range(nr_of_rooms):
        room_config[i] = dict(desc=input(f'{i+1}. Room description'),monster=input(f'{i+1}. Monster Name'))
    print(room_config)
    dungeon = initialize_rooms(room_config)
    for i in range(nr_of_rooms):
        res = dungeon[i].interact(player)
        if res:
            break
    print_results(player)
