#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys
    var = len(sys.argv)
    arg = sys.argv
    if var != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(arg[1])
        operator = arg[2]
        b = int(arg[3])
        if operator == '+':
            print("{:d} + {:d} = {:d}".format(a, b, calc.add(a, b)))
        elif operator == '-':
            print("{:d} - {:d} = {:d}".format(a, b, calc.sub(a, b)))
        elif operator == '*':
            print("{:d} * {:d} = {:d}".format(a, b, calc.mul(a, b)))
        elif operator == '/':
            print("{:d} / {:d} = {:d}".format(a, b, calc.div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
