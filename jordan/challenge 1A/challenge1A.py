# This is a simple calculator projects challenge from Braden
# This calculator should allow the user to input two numbers and choose whether they wish to add, substract, multiply, or divide them and then output the answer
# This calculator also gives the user the option to run another calculation if desired

def calculate():
    pass  #Unable to remove this line of code (can be anything so just chose 'pass') as then the next line errors out due to indenting. 
            #Any other indenting variations without this line results in a syntax error/the script not running correctly. NEEDS REVIEW FOR LEARNING
while True:
    print("Hi friend, this is a helpful calculator.") #Would prefer to have this line before the While Loop, but anything before the While Loop does not print. NEEDS REVIEW FOR LEARNING
    fNumber = int(input("Please type your first number: "))
    sNumber = int(input("Please type your second number: "))
    action = input("What would you like to do with these numbers? Add | Subtract | Multiply | Divide\nPlease type one of the options above: ")

    #If the user chooses to add the numbers
    if action == 'Add' or action == 'add':
        print("You have chosen to add. The final sum is: ", fNumber + sNumber)
        answer = input("Do you want to run another calculation?: ")
        if answer.lower().startswith("y"):
            print("OK, please continue.")
        elif answer.lower().startswith("n"):
            print("OK, bye!")
            exit()

    #If the user chooses to subtract the numbers
    elif action == 'Subtract' or action == 'subtract':
        print("You have chosen to subtract. The final sum is: ", fNumber - sNumber)
        answer = input("Do you want to run another calculation?: ")
        if answer.lower().startswith("y"):
            print("OK, please continue.")
        elif answer.lower().startswith("n"):
            print("OK, bye!")
            exit()

    #If the user chooses to multiply the numbers
    elif action == 'Multiply' or action == 'multiply':
        print("You have chosen to multiply. The final sum is: ", fNumber * sNumber)
        answer = input("Do you want to run another calculation?: ")
        if answer.lower().startswith("y"):
            print("OK, please continue.")
        elif answer.lower().startswith("n"):
            print("OK, bye!")
            exit()

    #If the user chooses to divide the numbers
    elif action == 'Divide' or action == 'divide':
        print("You have chosen to divide. The final sum is: ", fNumber / sNumber)
        answer = input("Do you want to run another calculation?: ")
        if answer.lower().startswith("y"):
            print("OK, please continue.")
        elif answer.lower().startswith("n"):
            print("OK, bye!")
            exit()

    #If the user inputs something invalid
    else:
        print("Please enter a valid input.")
        answer = input("Do you want to try again?: ")
        if answer.lower().startswith("y"):
            print("OK, please continue.")
        elif answer.lower().startswith("n"):
            print("OK, bye!")
            exit()
    pass   
        

           