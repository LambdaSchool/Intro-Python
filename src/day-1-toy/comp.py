# Write a list comprehension to produce the array [1, 2, 3, 4, 5]


y = [i for i in range (1, 6)]

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# x = [i**2 for i in y]
y = [i**3 for i in range(10)]
print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

w = [i.upper() for i in a]

print(w)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
# y = [if(i % 2 == 0) for i in x]
y = [i for i in x in inf(i) % 2 == 0]

print(y)

