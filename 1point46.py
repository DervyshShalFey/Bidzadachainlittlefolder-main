from transformation import *
try:
    x = float(input('Insert first edge of cuboid: '))
    if x <= 0:
        raise Exception
    x = transform(x)

    y = float(input('Insert second edge of cuboid: '))
    if y <= 0:
        raise Exception
    y = transform(y)

    z = float(input('Insert third edge of cuboid: '))
    if z <= 0:
        raise Exception
    z = transform(z)
    print(f'LSA: {transform(2*(x+y)*z)}')
    print(f'Volume: {transform(x*y*z)}')
except ValueError:
    print('Not a number!')
except Exception:
    print('Number can\'t be negative or be equal to zero!')