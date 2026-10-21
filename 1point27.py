from transformation import *
from math import *
try:
    x = float(input('Insert how high is point is space: '))
    if x <= 0:
        raise Exception
    x = transform(x)
    print(f'Distance: {transform(sqrt(2*6350*x+(x**2)))}')
except ValueError:
    print('Not a number!')
except Exception:
    print('Number can\'t be negative or be equal to zero!')