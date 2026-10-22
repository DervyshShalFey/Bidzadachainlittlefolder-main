from transformation import *
from math import *
try:
    one = []
    two = []
    x1 = float(input('Abscissae of first point: '))
    x1 = transform(x1)
    one.append(x1)
    y1 = float(input('Ordinate of first point: '))
    y1 = transform(y1)
    one.append(y1)
    x2 = float(input('Abscissae of second point: '))
    x2 = transform(x2)
    two.append(x2)
    y2 = float(input('Ordinate of second point: '))
    y2 = transform(y2)
    two.append(y2)
    print(f'First point{one}', end='; ')
    print(f'Second point{two}')
    print(f'Distance: {transform(sqrt((x2-x1)**2+(y2-y1)**2))}')
except ValueError:
    print('Not a number!')