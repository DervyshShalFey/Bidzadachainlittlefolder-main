from transformation import *
try:
    print('Vehicles are on one side')
    x = float(input('Insert speed of first vehicle in km/h: '))
    if x <= 0:
        raise Exception
    x = transform(x)

    y = float(input('Insert speed of second vehicle in km/h: '))
    if y <= 0:
        raise Exception
    y = transform(y)

    if x == y:
        raise ZeroDivisionError
    
    z = float(input('Distance between them in kms: '))
    if z <= 0:
        raise Exception
    z = transform(z)

    if x > y:
        print(f'Time needed them to meet: {transform(z+0.5*(x-y))} hours')
    elif y > x:
        print(f'Time needed them to meet: {transform(z-0.5*(x-y))} hours')
except ValueError:
    print('Not a number!')
except ZeroDivisionError:
    print('They will never meet, because they have the same speed')
except Exception:
    print('Number can\'t be negative or be equal to zero!')
