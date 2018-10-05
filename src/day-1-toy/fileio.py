# Use open to open file "foo.txt" for reading
f = open("foo.txt", "r")

# Print all the lines in the file
print(f.read())
# Close the file

f.close()

# Use open to open file "bar.txt" for writing
b = open("bar.txt", "w")

# Use the write() method to write three lines to the file
b.write(
    """
This is line 1
This is line 2
This is line 3
"""
)

# Close the file
b.close()
