from player import Player

class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def item_taken(self):
        print(f"{self.name} has been added to your inventory!")

    def item_dropped(self):
        print(f"{self.name} has been dropped!")

class Treasure(Item):
    def __init__(self, value, name):
        super().__init__(name)
        self.value = value

    def __str__(self):
        return self.name

    def remove_value(self):
        self.value = 0
