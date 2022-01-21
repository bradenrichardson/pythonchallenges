def calculate(ops_select=0, addends=[0,0]):

    print("Calculatron 4001")
    import operator
    ops = {
        "add": [operator.add," + "],
        "subtract": [operator.sub," - "],
        "multiply": [operator.mul," * "],
        "divide": [operator.truediv," / "]
    }

    if ops_select == 0:
        print("Would you like to add, subtract, multiply or divide two numbers? Please select one.")
        ops_select = input()
    ops_select = ops_select.casefold()

    while ops_select not in ops:
        print("Please select one of the following options: add, subtract, multiply or divide.")
        ops_select = input()
        ops_select = ops_select.casefold()
    ops_function = ops[ops_select]

    count = 0
    total = 0

    if addends == [0,0]:
        print("Which numbers would you like to {}?".format(ops_select))
        for n in addends:
            print("Number {}: ".format(operator.add(count,1)),end="")
            addends[count] = input()
            addends[count] = float(addends[count])
            if count == 0:
                total += addends[count]
            else:
                total = ops_function[0](total,addends[count])
            count += 1
    else:
        for n in addends:
            if count == 0:
                total += addends[count]
            else:
                total = ops_function[0](total,addends[count])
            count += 1

    addends_str = ops_function[1].join(map(str,addends))
    print("{} = {}".format(addends_str,total))

calculate()