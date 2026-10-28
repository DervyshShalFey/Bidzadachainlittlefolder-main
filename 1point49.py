#UNFINISHED
from transformation import *
from math import *
a = False
b = False
try:
    x = float(input('Insert bigger base: '))
    if x<=0:
        raise Exception
    y = float(input('Insert smaller base: '))
    if y<=0:
        raise Exception
    if y>=x:
        b = True
        raise Exception
    z = float(input('Insert angle of bigger base: '))
    if z<=0:
        raise Exception
    if z>=90:
        a = True
        raise Exception
    x = transform(x)
    y = transform(y)
    z = transform(z)
    print(f'Area of this trapezoid: {((x**2)-(y**2)/4)*tan(z)}')
except ValueError:
    print('Not a number!')
except Exception:
    if a == True:
        print('Angle can\'t be more than or be equal to ninety!')
    elif b == True:
        print('Smaller base can\'t be equal or be more than bigger base!')
    else:
        print('Number can\'t be negative or be equal to zero!')