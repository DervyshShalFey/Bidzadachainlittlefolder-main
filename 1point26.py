from transformation import *
try:
    x = float(input('Insert radius of circle: '))
    if x <= 0:
        raise Exception
    x = transform(x)
    print(f'Diameter: {transform(x*2)}')
except ValueError:
    print('Not a number!')
except Exception:
    print('Number can\'t be negative or be equal to zero!')