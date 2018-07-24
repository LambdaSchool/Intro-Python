import textwrap

from player import Player
from room import Room

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
def direction(d, curRoom):

    attrib = d + '_to'
    if hasattr(curRoom, attrib):
        return getattr(curRoom, attrib)

    # Otherwise print an error and stay in the same room
    print("You can't go that way")
    return curRoom

player = Player(room['outside'])

print(player.curRoom.name)

done = False

while not done:

    print("\n{}\n".format(player.curRoom.name))

    for line in textwrap.wrap(player.curRoom.description):
        print(line)

    s = input("\nCommand> ").strip().lower()

    if s == "q":
        done = True
    elif s in ["n", "s", "w", "e"]:
        player.curRoom = direction(s, player.curRoom)
    else:
        print("Unknown command {}".format(s))

