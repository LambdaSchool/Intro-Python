# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, playerName, startRoom):
        self.room = startRoom
        self.name = playerName