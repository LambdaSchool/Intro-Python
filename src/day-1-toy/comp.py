# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [i for i in range(1,6)]

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [1**3, 2**3, 3**3, 4**3, 5**3, 6**3, 7**3, 8**3, 9**3]
# y = [i**3 for i in range(10)]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = ["foo".upper(), "bar".upper(),"baz".upper()]
# y = [x.upper() for x in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [num for num in x if int(num) % 2 == 0]

print(y)

# completed