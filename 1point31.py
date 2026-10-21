from transformation import *
from math import *
try:
    x = float(input('Insert first number: '))
    x = transform(x)
    y = float(input('Insert second number: '))
    y = transform(y)
    print(f'Arithmetic mean: {transform((x+y)/2)}')
    print(f'Geometric mean: {transform(sqrt(x*y))}')
except ValueError:
    print('Not a number!')