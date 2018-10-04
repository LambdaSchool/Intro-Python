# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, label, name, description):
        self.name = name
        self.label = label
        self.description = description
        self.w_to = None
        self.a_to = None
        self.s_to = None
        self.d_to = None
        self.weaponsIn = []

    def directedRoom(self, direction):
        if direction == "w":
            return self.w_to
        elif direction == "a":
            return self.a_to
        elif direction == "s":
            return self.s_to
        elif direction == "d":
            return self.d_to
        else:
            return None

    def removeItem(self, weapon):
        for selectedWeapon in self.weaponsIn:
            if selectedWeapon.label == weapon:
                self.weaponsIn.remove(selectedWeapon)

    def __repr__(self):
        return f'{self.name} \n \n {self.description} '

    
