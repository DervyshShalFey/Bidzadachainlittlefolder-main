#UNFINISHED
from transformation import *
from math import *
try:
    x = float(input('Insert first number: '))
    x = transform(x)
    y = float(input('Insert second number: '))
    y = transform(y)
    z = float(input('Insert third number: '))
    z = transform(z)
    try:
        print(f'A) a = √(|e - (3/f)|^3 + g)  \n   If e is equal to {x}, f is equal to {y} and g is equal to {z}, then x will be equal to {transform(sqrt((module(x-(3/y))**3)+z))}')
    except ZeroDivisionError:
        print('A) Can\'t divide by zero!')
    except:
        print(f'A) Square root of |{x}-(3/{neg(y)})|^3+{pluey(z)}) is undefined.')
    try:
        print(f'Б) y = (|a|+2*sinus of b)/(5.5*a) \n   If a is equal to {x} and b is equal to {y}, then y will be equal to {(module(x)+2*sin(y))/(5.5*x)}')
    except ZeroDivisionError:
            print('Б) Can\'t divide by zero!')
except ValueError:
    print('Not a number!')