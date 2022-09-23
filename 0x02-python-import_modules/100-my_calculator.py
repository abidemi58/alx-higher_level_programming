#!/usr/bin/python3if __name__ == "__main__":
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
     num = len(sys.argv)
     if num != 4:
         print("Usage: ./100-my_calculator.py <a> <operator> <b>")
         exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op is '+':
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    elif op is '-':
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))
    elif op is '*':
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))
    elif op is '/':
        print("{} {} {} = {}".format(a, op, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
