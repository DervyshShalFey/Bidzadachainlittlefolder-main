from transformation import *
from math import *
try:
    x = float(input('Insert first number: '))
    x = transform(x)
    y = float(input('Insert second number: '))
    y = transform(y)
    try:
        print(f'A) x = (2/((a^2)+25)+b)/((√b)+((a+b)/2))  \n   If a is equal to {x} and b is equal to {y}, then x will be equal to {transform((2/(a**2)+25)+b)/((sqrt(b)+((a+b)/2)))}')
    except ZeroDivisionError:
        print('A) Can\'t divide by zero!')
    except:
        print(f'A) Square root of {y} is undefined.')
    try:
        print(f'Б) y = (|a|+2*sinus of b)/(5.5*a) \n   If a is equal to {x} and b is equal to {y}, then y will be equal to {(module(x)+2*sin(y))/(5.5*x)}')
    except ZeroDivisionError:
            print('Б) Can\'t divide by zero!')
except ValueError:
    print('Not a number!')