from transformation import *
from math import *
try:
    one = []
    two = []
    x1 = float(input('Abscissa of first point: '))
    x1 = transform(x1)
    one.append(x1)
    y1 = float(input('Ordinate of first point: '))
    y1 = transform(y1)
    one.append(y1)
    x2 = float(input('Abscissa of second point: '))
    x2 = transform(x2)
    two.append(x2)
    y2 = float(input('Ordinate of second point: '))
    y2 = transform(y2)
    two.append(y2)
    print(f'First point{one}', end='; ')
    print(f'Second point{two}')
    print(f'Distance: {transform(sqrt(coo(x1, x2)+coo(y1, y2)))}')
except ValueError:
    print('Not a number!')