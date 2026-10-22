from transformation import *
from math import *
try:
    x = float(input('Insert side of rectangle: '))
    if x <= 0:
        raise Exception
    x = transform(x)
    y = float(input('Insert other side of rectangle: '))
    if y <= 0:
        raise Exception
    y = transform(y)
    print(f'Perimeter: {transform((x+y)*2)}')
    print(f'Diagonal: {transform(sqrt((x**2)+(y**2)))}')
except ValueError:
    print('Not a number!')
except Exception:
    print('Number can\'t be negative or be equal to zero!')