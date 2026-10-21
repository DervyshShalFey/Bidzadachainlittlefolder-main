from transformation import *
try:
    x = float(input('Insert edge of cube: '))
    if x <= 0:
        raise Exception
    x = transform(x)
    print(f'LSA: {transform(4*(x**2))}')
    print(f'Volume: {transform(x**3)}')
except ValueError:
    print('Not a number!')
except Exception:
    print('Number can\'t be negative or be equal to zero!')