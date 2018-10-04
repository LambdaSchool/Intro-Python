from room import Room
from player import Player
import textwrap
from item import Item, Treasure

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
# Add some items

# Items aka weapons
wep1 = Item("sword", "a valerian steel sword")
wep2 = Item("bow", "an elvish bow with sharp arrows")

# Treasure Items (items subclass)
t1 = Treasure("diamonds", "a bag full of prestine diamonds", 500)
t2 = Treasure("gold", "a huge block of solid good.", 250)

playerStartingItems = [wep1]
room["outside"].addItem(wep2)

valid_directions = {"n": "n", "s": "s", "e": "e", "w": "w",
                    "forward": "n", "backwards": "s", "right": "e", "left": "w"}

player = Player(input("What is your name? "), room['outside'], playerStartingItems)
print(player.items)
print(player.currentRoom)

game_over = False

while not game_over:
    White ="\[\033[0;37m\]"
    cmds = input("-> ").lower().split(" ")
    # if command length is == 1
    if len(cmds) == 1:
        # print(cmds[0]) -- this just prints the command given
        # if user enters 'q' quit the game
        if cmds[0] == "q":
            print(f"{White} Game Over!")
            game_over = True
        # if command is found in valid-directions dictionary, travel
        elif cmds[0] in valid_directions:
            player.travel(valid_directions[cmds[0]])
        elif cmds[0] == "look":
            player.look()
        elif cmds[0] == "inventory":
            player.printInventory()
        else:
            print("I did not understand that command.")
    else:
        if cmds[0] == "look":
            if cmds[1] in valid_directions:
                player.look(valid_directions[cmds[1]])
        elif cmds[0] == "take":
            currentRoom = player.currentRoom
            wantedItem = currentRoom.getItemByName(cmds[1])
            if wantedItem is not None:    
                player.addItem(wantedItem)
                player.currentRoom.removeItem(wantedItem)
            else:
                print("You cannot see that item")
        elif cmds[0] == "drop":
            currentRoom = player.currentRoom
            discardedItem = player.getItemByName(cmds[1])
            if discardedItem is not None:
                player.removeItem(discardedItem)
                player.currentRoom.addItem(discardedItem)
            else:
                print("You are not holding that item")
        else:
            print("I did not understand that command.")
