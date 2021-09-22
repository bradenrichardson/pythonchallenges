## Challenges

# Ethan
# 2. Add functionality for multiplication, division and subtraction
def calculateSum(totalAddends):
    print("Calculatron 4000")
    print("Which numbers would you like to add together?")
    addends = list(range(totalAddends))
    sum = 0
    for n in addends:
        count = n + 1
        print("Number {}: ".format(count),end="")
        addends[n] = input()
        addends[n] = int(addends[n])
        sum += addends[n]
    addends_str = ' + '.join(map(str,addends))
    print("{} = {}".format(addends_str,sum))
    input()

# Jordan
# 1. Build a simple calculator
# - Print the sum of two user inputted values
def calculate():
    # Write your code here
    pass


# Braden
# 1. Create a program which allows a user to input any cryptocurrency ticker 
# and then receive an output of TRUE or FALSE as to whether that cryptocurrency
# is below the 50 Day EMA (Exponential Moving Average)


calculateSum(2)