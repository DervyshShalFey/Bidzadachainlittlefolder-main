
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
    print(f'Б) b = Sinus of e + (cosinus of h)^2\n   If e is equal to {x} and h is equal to {y}, then b will be equal to {sin(x)+(cos(y)**2)}')
    try:
        print(f'B) c = 33g/(ef - 3)\n   If e is equal to {x}, f is equal to {y} and g is equal to {z}, then x will be equal to {transform((33*z)/(x*y-3))}')
    except ZeroDivisionError:
        print('B) Can\'t divide by zero!')
except ValueError:
    print('Not a number!')