# importing room file into adv
from room import Room
# import player file into adv
from player import Player 

# Declare all the rooms
# an object called room holding a location string, and an instance of room
# each one has a value of a room object. imported above.
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
# setting up possible movements between rooms.
# can use these to create controls. 
# .x_to is a reference to another room. 
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

# a new instance of the player class. Passed with the params
# playerName = "Falcorn"
#startRoom = room['outside']
main_player = Player("Falcorn", room['outside'])

#start game a line down 
print("\n")
#player name should display at the top. 
print("Your player: " + main_player.name + " defender of the alliance \n")

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

# setting a flag. We can use this to make stuff work!
done = False

while not done:
    current_room = main_player.room 
    #room is what startRoom is set as. 
    #self.room = startRoom
    print(f'{current_room.name}\n{current_room.description}\n')

#ask for user input
#this is going to take all the white space off
#and convert the command to lowercase
    command = input("Command> ").strip().lower()
    