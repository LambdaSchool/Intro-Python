# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
{"lat":453324, "lon": 1234321, "name": "Big Joy"},
{"lat":453345, "lon": 9887034, "name": "Helly Toy"},
{"lat":453536, "lon": 1999984, "name": "Lish Moy"}
]

# Write a loop that prints out all the field values for all the waypoints

for i in waypoints:
    print(i["name"])
