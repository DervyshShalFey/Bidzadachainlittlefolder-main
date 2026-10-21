from transformation import *
from math import *
try:
    x = float(input('Insert inner radius: '))
    if x<=0:
        raise Exception
    y = float(input('Insert outer radius: '))
    if y<=0:
        raise Exception
    x = transform(x)
    y = transform(y)
    print(f'Area of this ring: {transform(3.14*((y**2)-(x**2)))}')
except ValueError:
    print('Not a number!')
except Exception:
    print('Number can\'t be negative or be equal to zero!')