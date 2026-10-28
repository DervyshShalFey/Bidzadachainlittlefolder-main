from transformation import *
from math import *
try:
    one, two, three, four = [], [], [], []
    print('Build a convex quadrilateral!')
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
    x4 = float(input('Abscissa of second point: '))
    transappend(x4, four)
    y4 = float(input('Ordinate of second point: '))
    transappend(y4, four)
    if one == two or two == three or one == three or one==four or two==four or three==four:
        raise Exception
    print(f'First point{one}', end='; ')
    print(f'Second point{two}', end='; ')
    print(f'Third point{three}', end='; ')
    print(f'Fourth point{four}')
    ABC = transform(0.5*module(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
    ACD = transform(0.5*module(x1*(y3-y4)+x3*(y4-y1)+x4*(y1-y3)))
    print(f'Area of convex quadrilateral: {ABC+ACD}')
    print(f'Area of first triangle: {ABC}')
    print(f'Area of second triangle: {ABC}')
except ValueError:
    print('Not a number!')
except Exception:
    print('Two points can\'t be in the same place!')