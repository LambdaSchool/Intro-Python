# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    latitute = 0
    longitute = 0

    def __init__(self, lat, lon):
        self.latitute = lat
        self.longitute = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    name = ''

    def __init__(self, n):
       self.name = n
       super().__init__(lat, lon)

    def __str__(self):
        return f"{self.name}, {self.latitute}, {self.longitute}"


# YOUR CODE HERE

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    difficulty = ''
    size = ''

    def __init(self, d, s):
       self.difficulty = d
       self.size = s
       super().__init__(lat, lon)
       
    def __str__(self):
        return f"{self.name}, {self.latitute}, {self.longitute}, {self.difficulty} , {self.size}"

# YOUR CODE HERE

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

Waypoint("Catacombs", 41.70505, -121.51521)

# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(Waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# YOUR CODE HERE

# Print it--also make this print more nicely
print(Geocache)
