# Write a function is_even that will return true if the passed in number is even.

# Read a number from the keyboard
num = input("Enter a number: ")
def isEven(num):
    if int(num) % 2 == 0:
        print('Even!')
        return True
    print('Odd!')
    return False
isEven(num)
# Print out "Even!" if the number is even. Otherwise print "Odd"
