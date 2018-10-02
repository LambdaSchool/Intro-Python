# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
class LatLon:
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.
class Waypoint(LatLon):
  def __init__(self, name, lat, lon):
    LatLon.__init__(self, lat, lon)
    self.name = name

  def __repr__(self):
    return f'{self.name}, {self.lat}, {self.lon}'

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
class Geocache(Waypoint):
  def __init__(self, name, difficulty, size, lat, lon):
    Waypoint.__init__(self, name, lat, lon)
    self.difficulty = difficulty
    self.size = size

  def __repr__(self):
    return f'{self.name}, {self.difficulty}, {self.size}, {self.lat}, {self.lon}'

# Make a new waypoint "Catacombs", 41.70505, -121.51521
w = Waypoint('Catacombs', 41.70505, -121.51521)
# Print it
# Without changing the following line, how can you make it print into something
# more human-readable?
print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
g = Geocache('Newberry Views', 1.5, 2, 44.052137, -121.41556)
# Print it--also make this print more nicely
print(g)
