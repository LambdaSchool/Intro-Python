# Use open to open file "foo.txt" for reading
f = open("foo.text", "r")
# Print all the lines in the file
print(f.read())
# Close the file
f.close()
# Use open to open file "bar.txt" for writing
f = open('bar.txt', 'w')
# Use the write() method to write three lines to the file
threelines = ["hm\n","hmm\n","hmmm\n",]
for i in threelines:
  f.write(i)
# Close the file
f.close()