# Write a function is_even that will return true if the passed-in number is even.

def even(x):
    if x%2 == 0:
        return True

# Read a number from the keyboard
num = input("Please submit a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def answer(num):
    if even(num):
        print("Even!")
    else:
        print("Odd")

answer(num)

