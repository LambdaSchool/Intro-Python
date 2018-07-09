x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

print('x is %d, y is %f, z is "%s"' % (x,y,z))
# Hooray python docs - https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting

# Use the 'format' string method to print the same thing
print('x is {}, y is {:.2f}, z is "{}"'.format(x,y,z))
