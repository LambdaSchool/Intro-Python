# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE

# This could be written also like this:
#newArray = []
#newArray.append(x + y)
# x = newArray

x += y
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE

x.insert(5, 99)  # We're making sure that we're specifying the index first and the number we want to add to the list.
print(x)

# Print the length of list x
# YOUR CODE HERE

print(len(x))
print(x.count)

# Print all the values in x multiplied by 1000
# YOUR CODE HERE

print(list(map(lambda a: a*1000, x)))