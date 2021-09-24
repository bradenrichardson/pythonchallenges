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

calculateSum(2)