#UNFINISHED
from transformation import *
from math import *
try:
    x = float(input('Insert first base: '))
    if x<=0:
        raise Exception
    y = float(input('Insert second base: '))
    if y<=0:
        raise Exception
    z = float(input('Insert angle of bigger base: '))
    if z<=0:
        raise Exception
    x = transform(x)
    y = transform(y)
    z = transform(z)
    print(f'Perimeter of this trapezoid: {transform(x+y+2*(sqrt((z**2)+(((x-y)/2)**2))))}')
except ValueError:
    print('Not a number!')
except Exception:
    print('Number can\'t be negative or be equal to zero!')