"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
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
# YOUR CODE HERE

waypoints.insert(3, {
        "lat": 999,
        "lon": -999,
        "name": "a fourth place"
    })  

    # waypoints.append({
    #     "lat": 999,
    #     "lon": -999,
    #     "name": "a fourth place"
    # })

print(waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE

# waypoints[1] = {
#         "lat": 7897897,
#         "lon": -789789,
#         "name": "not a real place"
#     }

# waypoints[0]["name"] = "not a real place"
waypoints[0].update({"name": "not a real place", "lon": -1500})

print(waypoints)

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
for data in waypoints:
    print(data["lat"], data["lon"], data["name"])

for item in waypoints:
    for el in item.values():
        print(el)