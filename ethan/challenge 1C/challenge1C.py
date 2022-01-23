def calculator(equation=0):

    import re
    import operator

    ops = {
        "*": operator.mul,
        "/": operator.truediv,
        "+": operator.add,
        "-": operator.sub
    }

    # Welcome screen text
    # # # # # # # # # # # # # # #
    print("Calculatron 4002.")
    print("---------------------------------------------------")
    print("SYNTAX. Add: +, Subtract: -, Multiply: *, Divide: /")
    print("e.g. x + y / z")
    print("---------------------------------------------------")
    print("Please type your equation below:")

    # Allow user to input equation if not passed through function
    # # # # # # # # # # # # # # #
    if equation == 0:
        equation = input()
    else:
        print(equation)
    equation = re.split(r"([*/+-])",equation)

    # Check for errors in the equation, and force the user to re-input equation if so
    # # # # # # # # # # # # # # #
    init_trigger = 0
    while init_trigger == 0 or ops_count == 0 or num_count == 0 or ops_count >= num_count or gap_check == 1 or invalid_char == 1:
        init_trigger = 1
        ops_count = 0
        num_count = 0
        gap_check = 0
        invalid_char = 0
        for element in equation:
            if element in ops:
                ops_count += 1
            if re.search(r"([0-9])",element):
                num_count += 1
            if re.search(r"([0-9])(?:\s+)([0-9])",element):
                gap_check = 1
            if re.search(r"[^\s1-9*/+-]",element):
                invalid_char = 1
        if ops_count == 0 or num_count == 0 or ops_count >= num_count or gap_check == 1 or invalid_char == 1:
            print("ERORR.")
            print("Please type a valid equation with just numbers and at least one of the following operators: +, -, *, /:")
            equation = input()
            equation = re.split(r"([*/+-])",equation)

    # Caculate the result
    # # # # # # # # # # # # # # #
    for key in ops:
        while key in equation:
            op_position = equation.index(key)
            num1_position = op_position - 1
            num2_position = op_position + 1
            number1 = float(equation[num1_position])
            number2 = float(equation[num2_position])
            result = ops[key](number1,number2)
            equation[op_position] = result
            del equation[num1_position]
            del equation[num2_position - 1]
    
    # Print the result
    # # # # # # # # # # # # # # #    
    print("= {}".format(result))

calculator()
# You can input your equation through the command-line after script execution,
# or pass it as a string through the function.
# e.g. calculator("x + y / z")