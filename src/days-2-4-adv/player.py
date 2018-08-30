# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, room):
    self.room = room
    self.items = []

  def removeItem(self, item):
    if len(self.items) > 0:
      self.items.remove(item)

  def addItem(self, item):
    self.items.append(item)