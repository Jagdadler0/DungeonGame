import Player
import Monster
import Room
def __main__():
    run_game(5)
def initialize_player(username):
    return Player.Player(username)
def initialize_rooms(rooms):
    ret_room = []
    for room in rooms:
        ret_room.append(Room.Room(rooms[room]['desc'],Monster.Monster(rooms[room]['monster'])))
    return ret_room
def print_results(player):
    print(f'The game is over!\nThank you for playing Dungeon Master!\nGood Bye!')
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

run_game(5)