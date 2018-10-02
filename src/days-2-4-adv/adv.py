from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

p = Player(input('What is your name?'), room['outside'])

# Write a loop that:
while True:
    currentRoom = p.currentRoom
    description = p.currentRoom.description
    def printErr():
        print('You\'ve run into a brick wall! Try another direction')
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    print('Where you are: ', currentRoom.name, ', What you see:', textwrap.fill(description))
    cmd = input('==>')
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    if cmd.upper() == 'N':
        if hasattr(currentRoom, 'n_to'):
            p.currentRoom = currentRoom.n_to
        else:
            printErr()
    elif cmd.upper() == 'S':
        if hasattr(currentRoom, 's_to'):
            p.currentRoom = currentRoom.s_to
        else:
            printErr()
    elif cmd.upper() == 'E':
        if hasattr(currentRoom, 'e_to'):
            p.currentRoom = currentRoom.e_to
        else:
            printErr()
    elif cmd.upper() == 'W':
        if hasattr(currentRoom, 'w_to'):
            p.currentRoom = currentRoom.w_to
        else:
            printErr()
#
# If the user enters "q", quit the game.
    elif cmd.upper() == 'Q':
        break;
