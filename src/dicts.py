# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
 {
   "lat": "48.8566 N",
   "lon": "2.3522 E",
   "name": "Paris"
 },
 {
   "lat": "33.8688 S",
   "lon": "151.2093 E",
   "name": "Sydney"
 },
]

# Write a loop that prints out all the field values for all the waypoints
for name in waypoints:
    print("The name of the waypoint is {[name]}.".format(name))