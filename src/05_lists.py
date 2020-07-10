# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]

x = [1, 2, 3, 4]

print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]

y = [1, 2, 3, 4, 8, 9, 10]

print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]

x = [1, 2, 3, 4, 9, 10]

print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]

x = [1, 2, 3, 4, 9, 99, 10]

print(x)

# Print the length of list x

print("Length of list x:", len(x))

# Print all the values in x multiplied by 1000

print("All values in x multiplied by 1000", [i*1000 for i in x])