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

book = Item("book", "dusty book of the occult in an unrecognizable language", 0)
candelabra = Item("candelabra", "a rusty piece of junk with no candles", 0)
dagger = Item("dagger", "bejeweled ceremonial dagger", 150)
rope = Item("rope", "length of rope; probably not long enough to rappel the cliff", 0)
gold = Item("gold", "small bag of gold coins", 100)

room['outside'].addItem(book)
room['foyer'].addItem(candelabra)
room['overlook'].addItem(dagger)
room['overlook'].addItem(rope)
room['narrow'].addItem(gold)


#
# Main
#
valid_directions = {"n": "n", "s": "s", "e": "e", "w": "w",
                    "forward": "n", "backward": "s", "right": "e", "left": "w"}
# Make a new player object that is currently in the 'outside' room.
player = Player(input("What is your name? "), room['outside'])
print(player.currentRoom)
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
    cmds = input("-> ").lower().split(" ")
    if len(cmds) == 1:
        if cmds[0] == "q":
            break
        elif cmds[0] in valid_directions:
            player.travel(valid_directions[cmds[0]])
        elif cmds[0] == "look":
            player.look()
        elif cmds[0] == "i" or cmds[0] == "inventory":
            player.printInventory()
        elif cmds[0] == "status":
            player.printStatus()
        else:
            print("I did not understand that command.")
    else:
        if cmds[0] == "look":
            if cmds[1] in valid_directions:
                player.look(valid_directions[cmds[1]])
        elif cmds[0] == "take":
            itemToTake = player.findItemByName(" ".join(cmds[1:]))
            if itemToTake is not None:
                player.addItem(itemToTake)
                player.totalScore(itemToTake)
                player.currentRoom.removeItem(itemToTake)
                print(f"You have picked up {itemToTake.name}")
            else:
                print("You do not see that item.")
        elif cmds[0] == "drop":
            itemToDrop = player.findItemByName(" ".join(cmds[1:]))
            if itemToDrop is not None:
                player.removeItem(itemToDrop)
                player.currentRoom.addItem(itemToDrop)
                print(f"You have dropped {itemToDrop.name}")
            else:
                print("You do not have that item.")
        else:
            print("I did not understand that command.")
