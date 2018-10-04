# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# [command here]
print(x.append(4), x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# [command here]
print(x.extend(y), x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# [command here]
print(x.remove(x[4]),  x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# [command here]
print(x.insert(len(x)-1, 99), x)

# Print the length of list x
# [command here]
print(len(x))

# Using a for loop, print all the element values multiplied by 1000
for i in x: 
    print(i * 1000)
