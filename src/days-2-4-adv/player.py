# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print(nextRoom)
        else:
            print("You cannot move in that direction.")
    def look(self, direction=None):
        if direction is None:
            print(self.currentRoom)
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:
                print(nextRoom)
            else:
                print("There is nothing there.")