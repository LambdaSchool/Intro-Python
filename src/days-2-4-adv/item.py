class Item:
    def __init__(self,name,description):
        self.name=name,
        self.description=description
    def __str__(self):
        return f'name:{self.name}\ndescription:{self.description}'
    def on_take(self):
        return None
class Treasure(Item):
    def __init__(self,name,description,value):
        super().__init__(name,description)
        self.value=value
        self.picked_up=False
    def on_take(self):
        if self.picked_up==False:
            self.picked_up=True
            return self.value
        else:
            return None