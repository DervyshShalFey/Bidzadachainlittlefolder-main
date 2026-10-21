from transformation import *
from math import *
try:
    x = float(input('Insert number of citizens: '))
    if x<=0:
        raise Exception
    y = float(input('Insert area of country(m^2): '))
    if y<=0:
        raise Exception
    x = transform(x)
    y = transform(y)
    print(f'Density of population in this country: {transform(x/y)}')
except ValueError:
    print('Not a number!')
except Exception:
    print('Number can\'t be negative or be equal to zero!')