# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, key, items=None, is_light=False):
        self.name = name
        self.description = description
        self.key = key
        self.items = items if items is not None else []
        self.is_light = is_light
