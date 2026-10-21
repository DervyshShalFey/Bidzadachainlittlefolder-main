from transformation import *
from math import *
try:
    x = float(input('Insert first number: '))
    x = transform(x)
    y = float(input('Insert second number: '))
    y = transform(y)
    try:
        print(f'A) z = (x + ((2 + y)/x^2))/(y+(1/(√((x^2)+10))))   \n   If x is equal to {x} and y is equal to {y}, then z will be equal to {transform((x+((2+y)/(x**2)))/(y+(1/(sqrt((x*2)+10)))))}')
    except ZeroDivisionError:
        print('A) Can\'t divide by zero!')
    print(f'Б) q = 2.8 * (sinus of x) + |y| \n   If x is equal to {x} and y is equal to {y}, then q will be equal to {2.8*(sin(x)+module(y))}')
except ValueError:
    print('Not a number!')