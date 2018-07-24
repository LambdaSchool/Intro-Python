from room import Room
from playerInfo import player
import os
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
player = Player(room['outside'])

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
direction = None
os.system("cls")
while True:
    flag = 0
    print(player.room)

    # switch statement... kind of
    direction = input("Where would you like to go? ")
    if direction == "north":
        if player.room.n_to:
            os.system("cls")
            choice = player.room.n_to
            flag = 1
    if direction == "south":
        if player.room.s_to:
            os.system("cls")
            choice = player.room.s_to
            flag = 1
    if direction == "east":
        if player.room.e_to:
            os.system("cls")
            choice = player.room.e_to
            flag = 1
    if direction == "west":
        if player.room.w_to:
            choice = player.room.w_to
            flag = 1
    if direction == "exit":
        os.system("cls")
        break
    if flag == 0:
        os.system("cls")
        print("You shall not pass!\n")
    if flag == 1:
        player.room = choice