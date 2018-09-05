# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description):
    self.name = name 
    self.description = description
    self.items = []
    self.n_to = None
    self.s_to = None
    self.e_to = None
    self.w_to = None
  def __str__(self):
    return f'\n---You are at the {self.name}---\n\n{self.description}\n Items in Area:\n{self.items}'
  def getRoomInDirection(self, direction):
    if direction == 'n':
      return self.n_to
    elif direction == 's':
      return self.s_to
    elif direction == 'e':
      return self.e_to
    elif direction == 'w':
      return self.w_to
    else:
      return None
  def connectRooms(self, destinationRoom, direction):
    if direction == 'n':
      self.n_to = destinationRoom
      destinationRoom.s_to = self
    elif direction == 's':
      self.s_to = destinationRoom
      destinationRoom.n_to = self
    elif direction == 'e':
      self.e_to = destinationRoom
      destinationRoom.w_to = self
    elif direction == 'w':
      self.w_to = destinationRoom
      destinationRoom.e_to = self
    else:
      print("invalid direction")
  def findItem(self, name):
    for i in self.items:
      if i.name == name:
        return i
      else:
        print('Sorry, I cannot find that item')  
  
  def addItem(self, item):
    self.items.append(item)
 
  def removeItem(self, item):
    self.items.remove(item)
      
    
    
    


