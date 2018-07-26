# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        'lat': 100,
        'lon': 200,
        'name': 'Teh Frawg!'
    },
    {
        'lat': 200,
        'lon': 100,
        'name': 'Teh Bawse!'
    },
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    }, 
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    }, 
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
new_waypoint = {
                    "lat": 36,
                    "lon": -112,
                    "name": "The Grand Canyon",
                    "index": 1
                }
waypoints.append(new_waypoint)

# Write a loop that prints out all the field values for all the waypoints
for i in waypoints:
    print('------------------------')
    for j in i:
        print(j, ':', i[j])