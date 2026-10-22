from transformation import *
from math import *
try:
    x = float(input('Insert first number: '))
    x = transform(module(x))
    y = float(input('Insert second number: '))
    y = transform(module(y))
    print(f'Arithmetic mean of their modules: {transform((x+y)/2)}')
    print(f'Geometric mean of their modules: {transform(sqrt(x*y))}')
except ValueError:
    print('Not a number!')