from transformation import *
from math import *
try:
    x = float(input('Insert volume of object: '))
    if xy<=0:
        raise Exception
    y = float(input('Insert weight of object: '))
    if y<=0:
        raise Exception
    x = transform(x)
    y = transform(y)
    print(f'Density of material the object is made of: {transform(y/x)}')
except ValueError:
    print('Not a number!')
except Exception:
    print('Number can\'t be negative or be equal to zero!')