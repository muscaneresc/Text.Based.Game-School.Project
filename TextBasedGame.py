#  Sonny Muscanere

rooms = {  # Dictionary for Rooms
        'Keep Entrance': {'east': 'Hall of the Serpent'},
    
        'Hall of the Serpent': {'east': 'Courtyard of the Lion',
                                'south': "Guards' Armory",
                                'north': 'Stairwell',
                                'west': 'Keep Entrance',
                                'item': 'helmet'},

        "Guards' Armory": {'north': 'Hall of the Serpent',
                           'item': 'tower_shield'},

        'Stairwell': {'south': 'Hall of the Serpent',
                      'east': 'Hall of the Goat',
                      'item': 'longsword'},

        'Hall of the Goat': {'west': 'Stairwell',
                             'east': 'Library',
                             'north': 'Balcony',
                             'south': 'Courtyard of the Lion',
                             'item': 'chain_mail'},
        'Balcony': {'south': 'Hall of the Goat',
                    'item': 'bow_and_quiver'},

        'Library': {'west': 'Hall of the Goat',
                    'item': 'fire_potion'},

        'Courtyard of the Lion': {'west': 'Hall of the Serpent',
                                  'north': 'Hall of the Goat',
                                  'item': 'Chimera'}
    }

#  Player Inventory
inventory = []

#  Start player at the Keep Entrance
current_room = 'Keep Entrance'

# 1 for Finish, 0 for Loop
player_finish = 0


#  Functions
def player_status():  # Room status
    """This function defines the player status and displays it to the player between moves."""

    r = current_room
    i = 'item'
    if r == 'Courtyard of the Lion':
        print('You are in the {}. You have encountered the beast!'.format(r))
    elif i in rooms[r]:
        print('You are in the {}. This room contains a {}.'.format(r, rooms[r][i]))
    elif i not in rooms[r]:
        print('You are in the {}. There is no item in this room.'.format(r))
    print('Inventory:', inventory)


def room_move():  # Move rooms
    """This function defines the movement command of the player when inputting to go a direction."""

    r = current_room
    d = command[1]  # Direction input
    avail_dirs = list(rooms[r].keys())  # Available directions in current room
    if d in avail_dirs:
        r = rooms[r][d]
        return r
    else:
        print('You can not do that.\n')
        return r


def get_item():  # Obtain an item
    """This function defines the get command of the player when inputting to obtain an item."""

    r = current_room
    i = command[1]  # Item input
    if 'item' not in rooms[r]:
        print('That item is not here.\n')
        return
    elif i == rooms[r]['item']:
        inventory.append(rooms[r]['item'])
        del rooms[r]['item']
        print(i, 'obtained!\n')
    elif i != rooms[r]['item']:
        print('That item is not here.\n')


def main_menu():
    """The main menu and beginning message of the game."""

    print('Welcome to the Keep of the Chimera. The beast rests here within.\n' 
          'Acquire all of the items to slay the beast. Otherwise, perish.')
    print('Player commands:\n'
          '     go north\n'
          '     go south\n'
          '     go east\n'
          '     go west\n'
          '     get [item name]\n'
          '     exit')
    print('-' * 35)
    print('You begin at the entrance to the Keep with an empty inventory.')


if __name__ == '__main__':
    #  Main Menu
    main_menu()
    command = input('Enter your command:\n').lower().split()

    #  Game loop
    while player_finish != 1:
        if command[0] == 'exit':  # Exit command
            player_finish = 1
            break
        elif command[0] == 'go':  # Move rooms
            current_room = room_move()
        elif command[0] == 'get':  # Get item
            get_item()
        else:
            print('You can not do that.\n')
        player_status()
        if current_room == 'Courtyard of the Lion':
            if len(inventory) == 6:  # Player wins
                print('You approach the beast with all items obtained.\n'
                      'After a fearsome battle, you have slain the Chimera!')
                player_finish = 1
                break
            else:  # Player loses
                print('You have not yet acquired all of the items!\n'
                      'You have been slain by the Chimera.')
                player_finish = 1
                break
        command = input('Enter your move:\n').split()
