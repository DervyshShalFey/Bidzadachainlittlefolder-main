from transformation import *
from math import *
try:
    one, two, three = [], [], []
    print('Build a traingle!')
    x1 = float(input('Abscissa of first point: '))
    transappend(x1, one)
    y1 = float(input('Ordinate of first point: '))
    transappend(y1, one)
    x2 = float(input('Abscissa of second point: '))
    transappend(x2, two)
    y2 = float(input('Ordinate of second point: '))
    transappend(y2, two)
    x3 = float(input('Abscissa of second point: '))
    transappend(x3, three)
    y3 = float(input('Ordinate of second point: '))
    transappend(y3, three)
    if one == two or two == three or one == three:
        raise Exception
    print(f'First point{one}', end='; ')
    print(f'Second point{two}', end='; ')
    print(f'Third point{three}')
    XY = transform(sqrt(coo(x1, x2)+coo(y1, y2)))
    YZ = transform(sqrt(coo(x2, x3)+coo(y2, y3)))
    ZX = transform(sqrt(coo(x3, x1)+coo(y3, y1)))
    print(f'Perimeter: {transform(XY+YZ+ZX)}')
    print(f'Area: {transform(0.5*module(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))}')
except ValueError:
    print('Not a number!')
except Exception:
    print('Two points can\'t be in the same place!')