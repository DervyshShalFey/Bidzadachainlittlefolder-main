from math import *
from transformation import *
try:
    x = float(input('Insert a number: '))
    x = transform(x)
    try:
        print(f'y = (a^2 + 10)  / (√a^2 - 1) \nIf a is equal to {x}, then y will be equal to {transform((x**2+10)/(sqrt((x**2)-1)))}')
    except ZeroDivisionError:
        print('Can\'t divide by zero!')
    except:
        print(f'Square root of a^2 - 1, where a = {x} is undefined')
except ValueError:
    print('Not a number!')