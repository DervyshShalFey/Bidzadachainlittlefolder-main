from transformation import *
try:
    print('Vehicles are across each other')
    x = float(input('Insert speed of first vehicle in km/h: '))
    if x <= 0:
        raise Exception
    x = transform(x)

    y = float(input('Insert speed of second vehicle in km/h: '))
    if y <= 0:
        raise Exception
    y = transform(y)

    z = float(input('Distance between them in kms: '))
    if z <= 0:
        raise Exception
    z = transform(z)

    print(f'Time needed them to meet: {transform(z/(x+y))}')
except ValueError:
    print('Not a number!')
except Exception:
    print('Number can\'t be negative or be equal to zero!')