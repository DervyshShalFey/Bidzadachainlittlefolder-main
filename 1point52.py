from transformation import *
from math import *
try:
    x = float(input('KG of candies bought: '))
    if x < 0:
        raise ZeroDivisionError
    x = transform(x)

    x2 = float(input('Cost of candies per KG in $: '))
    if x2 <= 0:
        raise Exception
    x2 = transform(x2)

    y = float(input('KG of cookies bought: '))
    if y < 0:
        raise ZeroDivisionError
    y = transform(y)

    y2 = float(input('Cost of cookies per KG in $: '))
    if y2 <= 0:
        raise Exception
    y2 = transform(y2)

    z = float(input('KG of apples bought: '))
    if z < 0:
        raise ZeroDivisionError
    z = transform(z)

    z2 = float(input('Cost of apples per KG in $: '))
    if z2 <= 0:
        raise Exception
    z2 = transform(z2)

    print(f'You must pay {transform(x*x2+y*y2+z*z2)}$ to buy it!')
except ValueError:
    print('Not a number!')
except ZeroDivisionError:
    print('Number can\'t be equal to zero!')
except Exception:
    print('Number can\'t be negative or be equal to zero!')