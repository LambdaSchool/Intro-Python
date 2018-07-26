from room import Room
from player import Player
from item import Item
import textwrap
import sys
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'bridge': Room("Bridge", """Rough winds blow acoss a lonely bridge. The smell of dragon fire and brimstone is heavy here.
On the other side you see a red dragon sleeping in the sunlight. It guards the entrance to an ancient cathedral""", []),

    'cathedral': Room("Cathedral", """Broken pews, torn tapestries, and skeletons of past adventurers are all that remain inside.
At the end, sunlight illuminates the lady's chapel. You see a crack in the wall.""", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("torch", "an everlasting torch that gives off a yellow light"), Item("potion", "a bright red potion"), 
Item("parchment", "dusy, yello parchment that's ready to disintegrate")]),

    'armory': Room("Armory", """You find a small armory filled with rusted weapons and some tools. At the far end lies a locked chest
and a blackened shield. You find an encryption on the chest lid: 'The ancient hero offers his sword but only to those he deems worthy'""", [
Item("shield", "a battered steel shield that's been blackened with fire")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("sword", "a broadsword fit for a hero")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("key", "a simple brass key")]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].e_to = room['bridge']
room['bridge'].w_to = room['outside']
room['bridge'].n_to = room['cathedral']
room['cathedral'].s_to = room['bridge']
room['cathedral'].n_to = room['narrow']
room['armory'].e_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['armory']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['narrow'].s_to = room['cathedral']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Justin", room['outside'])
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

general_inputs = ["q", "i"] # valid general inputs
move_inputs = ["n", "e", "s", "w"] # valid inputs to advance game
item_inputs = ["get", "take", "drop"] # valid item interactions

quit = False # describes overall game state

while not quit:
	current = player.room
	description = textwrap.fill(current.description)
	# show player the room they are in
	print("{0}\n{1}".format(current.name, description))
	# show player all items available in current room
	if len(current.items) > 0:
		for item in current.items:
			print("You see:\n\ta {0}\n\t{1}".format(item.showName(), item.showDescription()))
	else:
		print("There are no items in this room")
	# take player commands and remove formatting
	player_input = input("Command: ").strip().lower()
	# separate player commands into verb + noun
	parsed = player_input.split(" ")

	# Single Word Command Input Parsing
	if len(parsed) == 1:
		if parsed[0] in general_inputs:
			# player quits/exits game
			if parsed[0] == "q" or parsed[0] == "quit":
				quit = True
			# show player inventory
			if parsed[0] == "i":
				print("You have the following items: {0}".format(player.inventory)) 
		elif parsed[0] in move_inputs:
			dirAttr = parsed[0] + "_to"
			# check if move input is valid
			if hasattr(current, dirAttr):
				player.room = getattr(current, dirAttr) # update player's location
			else:
				# invalid room change
				print("You can't go that way!")
		else:
			# unknown single command
			print("That command doesn't make sense!")

	# Two Word Command Input Parsing
	elif len(parsed) == 2:
		verb = parsed[0] # action player takes with an item
		noun = parsed[1] # noun itself

		if verb in item_inputs:
			if verb == "get" or verb == "take":
				for index, item in enumerate(current.items):
					if item.name == noun:
						# remove item from room
						current.items.remove(current.items[index])
						# add item to player inventory
						player.inventory.append(item)
			if verb == "drop":
				for index, item in enumerate(player.inventory):
					if item.name == noun:
						# remove item from player inventory
						player.inventory.remove(player.inventory[index])
						# add item to room
						current.items.append(item)
		else:
			print("You can't do that with an item!")
	else:
		print("That doesn't mean anything!")















