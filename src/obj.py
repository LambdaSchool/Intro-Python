# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# class MyParentClass():
#     def __init__(self, x, y):
#     pass

# class SubClass(MyParentClass):
#     def __init__(self, x, y):
#     super().__init__(x, y)


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon



# # Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# # constructor. It should inherit from LatLon.

class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name
    
    def __str__(self):
        return "Cache {} is located at {}, {}".format(x, y, z)
    


    
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# # `size`, `lat`, and `lon` to the constructor. Wphat should it inherit from?
x = "Catacombs"
y = 44.05137
z = -121.41556
a = 1.2
b = 3

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size
    def __str__(self):
        return "Cache {0} is located at {1}, {2} and is {3} in size and {4} in difficulty".format(x, y, z, a, b)
    
# # Make a new waypoint "Catacombs", 41.70505, -121.51521

w = Waypoint(44.05137, -121.41556, "Catacombs")
# # Print it
# #
# # Without changing the following line, how can you make it print into something
# # more human-readable?
print(w)

# # Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
g = Geocache(44.052137, -121.41556, "Newberry Views", 1.5, 2).__str__()
# # Print it--also make this print more nicely
print(g)

