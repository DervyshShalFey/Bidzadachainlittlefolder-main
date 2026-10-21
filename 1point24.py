from math import *
from transformation import *
try:
    x = float(input('Insert a number: '))
    x = transform(x)
    try:
        print(f'A) x = √(2a + sinus of |3a|)/3.56 \n   If a is equal to {x}, then x will be equal to {sqrt((2*x + sin(module(3*x)))/3.56)}')
    except:
        print(f'A) Square root of (2a + sinus of |3a|)/3.56, where a = {x} is undefined')
    try:
        print(f'Б) y = Sinus of (3.2 + √(1 + x))/(|5x|)\n   If x is equal to {x}, then y will be equal to {sin((3.2+sqrt(1+x))/(5*module(x)))}')
    except ZeroDivisionError:
        print('Б) Can\'t divide by zero!')
    except:
        print(f'Б) Square root of 1 + x, where x = {x} is undefined')
except ValueError:
    print('Not a number!')