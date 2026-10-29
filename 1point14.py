from math import *
from transformation import *

try:
    x = float(input('Insert number: '))
    x = transform(x)


    print(f'A) {neg(x)} * 2 = {transform(2*x)}')

    print(f'Б) Sinus of {x}: {sin(x)}')

    print(f'В) {x} ^ 2 = {transform(x**2)}')

    try:
        print(f'Г) √{x} = {transform(sqrt(x))}')
    except:
        print(f'Г) Square root of {x} is undefined')

    print(f'Д) |{x}| = {transform(module(x))}')

    print(f'Е)5 * cosinus of {x} = {5*cos(x)}')
    
    print(f'Ж)-7\'5 * {neg(x)} ^ 2 = {-7.5*x**2}')
    
    try:
        print(f'3)3 *  √{x} = {3*transform(sqrt(x))}')
    except:
        print(f'3) Square root of {x} is undefined')

    y = float(input('Insert 2nd number: '))
    y = transform(y)


    print(f'И) sin{x} * cos{y} + cos{x} * sin{y}: {sin(x)*cos(y)+cos(x)*sin(y)}')

    try:
        print(f'K){x} *  √{2*neg(y)} = {x*transform(sqrt(2*y))}')
    except:
        print(f'K) Square root of {y} is undefined')

    print(f'Л) 3 * sin{2*x} * cos{3*y} = {3*sin(2*x)*cos(3*y)}')

    try:
        print(f'М)-5 *  √{x}+√{y} = {-5*transform(sqrt(x+sqrt(y)))}')
    except:
        print(f'М) Square root of either {x} or {y} is undefined')

except ValueError:
    print('Not a number!')