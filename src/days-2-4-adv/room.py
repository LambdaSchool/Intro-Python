# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return self.name
    def getDescription(self):
        wrapper = textwrap.TextWrapper(initial_indent="* ", width=40, subsequent_indent="* ")
        return wrapper.fill(self.description) + "\n"
    def direction(self, direction):
        if direction == 'N':
            return self.n_to
        elif direction == 'S':
            return self.n_to
        elif direction == 'E':
            return self.n_to
        elif direction == 'W':
            return self.n_to
        else:
            return None
    def validMoves(self):
        valid = {}
        if self.n_to:
            valid.update(North = self.n_to)
        if self.s_to:
            valid.update(South = self.s_to)
        if self.e_to:
            valid.update(East = self.e_to)
        if self.w_to:
            valid.update(West = self.w_to)
        return valid