a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print(a[1])

# Output the second-to-last element: 9
print(a[-2])

# Output the last three elements in the array: [7, 9, 6]
print(a[-3:])

# Output the two middle elements in the array: [1, 7]
print(a.pop((len(a) -1) //2))


# Output every element except the first one: [4, 1, 7, 9, 6]
a.pop(0)
print(a)

# Output every element except the last one: [2, 4, 1, 7, 9]
a.pop(-1)
print(a)

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"ß
print(s[7:12])