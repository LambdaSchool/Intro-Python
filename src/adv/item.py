# Add an `Item` class in a file `item.py`.

# This will be the _base class_ for specialized item types to be declared
# later.

# The item should have `name` and `description` attributes.

# Hint: the name should be one word for ease in parsing later.

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.dropped = False
    
    def __repr__(self):
        return self.name

    def on_take(self):
        print('Hello')


class Treasure(Item):
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def on_take(self):
        return self.value
