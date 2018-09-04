# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None
    def addItem(self, item):
        self.items.append(item)
    