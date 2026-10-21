from transformation import *
try:
    x = float(input('Insert side of square: '))
    if x <= 0:
        raise Exception
    x = transform(x)
    print(f'Perimeter: {transform(x*4)}')
except ValueError:
    print('Not a number!')
except Exception:
    print('Number can\'t be negative or be equal to zero!')