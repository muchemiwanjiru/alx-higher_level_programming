#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
# calculator by john for john's
if __name__ == '__main__':

    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>'.format())
        exit(1)
    if sys.argv[2] not in '+-*/':
        print('Unknown operator. Available operators: +, -, * and /'.format())
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    operator = sys.argv[2]
    if operator == '+':
        print('{:d} {} {:d} = {:d}'.format(a, operator, b, add(a, b)))
    elif operator == '-':
        print('{:d} {} {:d} = {:d}'.format(a, operator, b, sub(a, b)))
    elif operator == '*':
        print('{:d} {} {:d} = {:d}'.format(a, operator, b, mul(a, b)))
    else:
        print('{:d} {} {:d} = {:d}'.format(a, operator, b, div(a, b)))


















