from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ['sword']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['shield']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['flint']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['stick']),
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
player = Player(input("What is your character's name?   "), room['outside'], [])
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
    print(f'\nLocation: {player.location.name}')
    print(f'{player.location.description}')
    if len(player.location.items) > 0:
        player.location.print_items()

    player_input = input(f'\nWhat does {player.name} do?   ')

    if len(player_input) < 1:
        print('\nControls: N,S,E,W to move to a different room. P to pick up an item. I to view your inventory. Q to quit')
    elif player_input[0].lower() == "q":
        break
    elif player_input[0].lower() == "n" or player_input[0].lower() == "s" or player_input[0].lower() == "w" or player_input[0].lower() == "e":
        player.change_location(player_input[0])
    elif player_input[0].lower() == "t" or player_input[0].lower() == "p":
        if len(player.location.items) > 0:
            player.take_item(player.location.items[0])
            player.location.remove_item(player.location.items[0])
        else:
            print("There are nothing you can pick up in this room")
    elif player_input[0].lower() == "i":
        player.view_inventory()
    else:
        print('\nControls: N,S,E,W to move to a different room. Q to quit')
