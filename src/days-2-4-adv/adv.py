from room import Room
from player import Player
from items import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 
                     [Item("Map of the Location")]),
 
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
[Item("Coin of the Treasure")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
[Item("Photo of the deceased owner")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
[Item("Backpack belonging to other Adventurers")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
[Item("List of different treasure spots left by the other adventurers")]),
}
#Create item dictionary
# item = {
#     "Map": Item("Map of the Location"),

#     "Coin": Item("Coin of the Treasure"),

#     "Photo": Item("Photo of the deceased owner"),

#     "Backpack": Item("Backpack belonging to other Adventurers"), 

#     "List": Item("List of different treasure spots left by the other adventurers")
# }


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'], [Item("Map of the Location")])
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

while True: 
    print("Begin your journey")
    print("Chose your direction by pressing n for North, s for South, e for East, w for West, or you can chose q and end your journey now")

    direction = input("-->  ").toLower().split(" ")

    if direction == 'q':
        print("\nYour Journey has ended")
        break
    elif direction == 'n':
        if not hasattr(player.currentRoom.n_to, 'name'):
         print('\n Dead End')
        else:
            player.currentRoom = player.currentRoom.n_to 
            print(f"""{player.currentRoom.name}:
            {player.currentRoom.description}""")
    elif direction == 's':
        if not hasattr(player.currentRoom.s_to, 'name'):
         print('\n Dead End')
        else:
            player.currentRoom = player.currentRoom.s_to
            print(f"""{player.currentRoom.name}:
            {player.currentRoom.description}""")
    elif direction == 'w':
        if not hasattr(player.currentRoom.w_to, 'name'):
         print('\n Dead End')
        else:
            player.currentRoom = player.currentRoom.w_to 
            print(f"""{player.currentRoom.name}:
            {player.currentRoom.description}""")  
    elif direction == 'e':
        if not hasattr(player.currentRoom.e_to, 'name'):
         print('\n Dead End')
        else:
            player.currentRoom = player.currentRoom.e_to   
            print(f"""{player.currentRoom.name}:
            {player.currentRoom.description}""")        