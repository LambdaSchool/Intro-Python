# Use open to open file "foo.txt" for reading
file = open("foo.txt", "r")
# Print all the lines in the file
print(file.read())
# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file = open("foo.txt", "w")

# Use the write() method to write three lines to the file
file.write("Hi. Hi. Hi again. Bye.")

# Close the file
file.close()