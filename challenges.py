## Challenges

# Ethan
# 2. Add functionality for multiplication, division and subtraction
# 3. Allow any number of user inputs from the command line ie. 4 + 7 * 31 + 433 - 45 = 609
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


calculateSum(2)