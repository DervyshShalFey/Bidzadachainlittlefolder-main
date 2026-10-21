from transformation import *
from math import *
try:
    x = float(input('Insert first leg: '))
    if x<=0:
        raise Exception
    y = float(input('Insert second leg: '))
    if y<=0:
        raise Exception
    x = transform(x)
    y = transform(y)
    print(f'Hypotenuse of this right-angled traingle: {transform((sqrt((x**2)+(y**2))))}')
except ValueError:
    print('Not a number!')
except Exception:
    print('Number can\'t be negative or be equal to zero!')