class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return f"{self.name} - {self.description}"
    def __str__(self):
        return f"{self.name}"
    def getDescription(self):
        return self.description