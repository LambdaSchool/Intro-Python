# Write a function is_even that will return true if the passed in number is even.

# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"
def isEven(num):
    if(num % 2 == 0):
        print("Even!")
        return;
    else: 
        print("Odd!")
        return;

isEven(int(num))
