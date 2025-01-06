import Player
import Monster
import Room
import random
def __main__():
    run_game(5)
def initialize_player(username):
    return Player.Player(username, random.randint(40,80), 100)
def initialize_rooms(rooms):
    ret_room = []
    for room in rooms:
        monster = Monster.Monster(rooms[room]['monster'], random.randint(20,40), random.randint(40,80))
        ret_room.append(Room.Room(rooms[room]['desc'],monster))
    return ret_room
def print_results(player):
    print('---------------------------------------------')
    print('The game is over!')
    print(player)
    print('Thank you for playing Dungeon Master!')
    print('Good Bye!')
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
