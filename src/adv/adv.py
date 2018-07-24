import os
from time import sleep
from textwrap import wrap

from room import Room
from player import Player

# Declare all the rooms

room = {
    #outside:   { name: "Outside Cave Entrance", description: "North of you, the cave mount beckons", n_to: {POINTS TO FOYER}}
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer","Dim light filters in from the south. Dusty passages run north and east."),
    'overlook': Room("Grand Overlook","A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),
    'narrow':   Room("Narrow Passage","The narrow passage bends here from west to north. The smell of gold permeates the air."),
    'treasure': Room("Treasure Chamber","You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
    # Add your own room here
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

# DEBUG
# print(room['outside'].s_to)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
#           { name: 'Moises', location: SOME OBJECT REFERENCE }
player = Player('Moises', room['outside'])


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

while(True):
    # Clear the console so it is more immersive    
    os.system('cls' if os.name == 'nt' else 'clear')
    direction = None
    print(
        '\nYou are located at:','\n'.join(wrap(player.location.name, width=50)),
        '\nDescription:', '\n'.join(wrap(player.location.description, width=50)))
    direction = input("\nIn what direction do you wish to proceed\n(N,E,W,S) or (Q: for quitting) pick one: ").lower()
    player.move_to(direction)
