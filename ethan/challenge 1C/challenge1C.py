import argparse
import operator
import re

def get_equation():
    def equation_inputs(arg_value, pat=re.compile(r"[0123456789*/+-.]+")):
        if not pat.fullmatch(arg_value):
            raise argparse.ArgumentTypeError("You entered an invalid character.\n Please ensure your equation contains only numbers, decimal points and these operators:\n* / + -")
        return arg_value
    parser = argparse.ArgumentParser(description="This is a calculator which allows you to multiply, divide, add and subtract any numbers with a single argument. Parentheses are not supported.")
    parser.add_argument("equation", type=equation_inputs, nargs=1, help="enter equation with operators [*/+-] e.g. '2+2/4'")
    args = parser.parse_args()
    args = vars(args)
    equation = args["equation"][0]
    return equation

def calculate(equation):
    ops = {
    "*": operator.mul,
    "/": operator.truediv,
    "+": operator.add,
    "-": operator.sub
    }
    equation = re.split(r"([*/+-])",equation)
    try:
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
        print(result)
    except (ValueError):
        print("error: There are too many operators in your equation.\nPlease ensure your equation does not have more operators than operands.")
    except (ZeroDivisionError):
        print("error: You can't divide 0 by 0. It simply cannot be done. I'll bet money.")
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        errormessage = template.format(type(ex).__name__, ex.args)
        print(errormessage)

def main():
    calculate(get_equation())

if __name__ == "__main__":
    main()