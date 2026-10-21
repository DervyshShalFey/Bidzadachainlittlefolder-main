from transformation import *
from math import *
try:
    x = float(input('Insert 1st number: '))
    y = float(input('Insert 2nd number: '))
    x = transform(x)
    y = transform(y)
    print(f'ax + b = 0 \nIf a is equal to {x} and b is equal to {y}, then x will be equal to {transform(-y/x)}')
except ValueError:
    print('Not a number!')
except ZeroDivisionError:
    print(f'ax + b = 0\na can\'t be equal to zero!')