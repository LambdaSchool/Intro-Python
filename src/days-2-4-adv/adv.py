from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     """North of you, the cave mount beckons"""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['outside'].add_item(Item('Backpack', 'A backpack to hold your items'))
room['treasure'].add_item(Item('Sword', 'A rusty sword.'))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

valid_directions = {'n': 'n', 's': 's', 'e': 'e', 'w': 'w', 'forward': 'n', 'backwards': 's', 'right': 'e', 'left': 'w'}

p = Player(input('What is your name? \n'), room['outside'])
print(p.room)
p.room.room_items()

while True:
    cmd = input('-> ').lower().split(' ')
    if len(cmd) == 1:
        if cmd[0] == 'q':
            break
        elif cmd[0] in valid_directions:
            p.move(valid_directions[cmd[0]])
        else:
            print('That is not a valid command. Please try again.')
    else:
        if cmd[0] == 'look':
            if cmd[1] in valid_directions:
                p.look(valid_directions[cmd[1]])
        elif cmd[0] == 'get' or cmd[0] == 'take':
            p.get_item(cmd[1])
        else:
            print('That is not a valid command. Please try again.')
