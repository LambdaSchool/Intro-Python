# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location, inventory):
        self.name = name
        self.location = location
        self.inventory = inventory

    def __str__(self):
        return self.name

    def get_location(self, location):
        return self.location

    def change_location(self, direction):
        new_location = self.location.next_room(direction)
        if new_location == None:
            print("\nThere is nothing in that direction")
        else:
            self.location = new_location

    def take_item(self, item):
        self.inventory.append(item)

    def view_inventory(self):
        print(f"{self.name} is currently holding:")
        for item in self.inventory:
            print(f"{item}")
