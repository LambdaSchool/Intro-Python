from room import Room
from player import Player

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


'''room['outside'].connectRooms(room['foyer'], "n")
room['foyer'].connectRooms(room['overlook'], "n")
room['foyer'].connectRooms(room['outside'], "s")
room['foyer'].connectRooms(room['narrow'], "e")
room['overlook'].connectRooms(room['foyer'], "s")
room['narrow'].connectRooms(room['foyer'], "w")
room['narrow'].connectRooms(room['treasure'], "n")
room['treasure'].connectRooms(room['narrow'], "s")
'''
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

name = input("What is your name? ")

player = Player(name, room['outside'])

print (f"Welcome, {player.name}!\n")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

while True:
    print (f"\n  {player.location.title}\n    {player.location.description}\n" )
    inp = input("What is your command: ")
    if inp == "q":
        break
    if inp == "n" or inp == "s" or inp == "w" or inp == "e":
        newRoom = player.location.getRmInDir(inp)
        if newRoom == None:
            print("You cannot move in that direction")
        else:
            player.changeLocation(newRoom)
    else:
        print('That command is not recognized.')
    
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
