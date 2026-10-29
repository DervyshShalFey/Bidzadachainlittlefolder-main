from transformation import *
try:
    x = float(input('Insert degrees in C: '))
    if x < -237.15:
        raise Exception
    x = transform(x)

    print(f'F: {transform(round((1.8*x+32), 2))}')
    print(f'K: {transform(round((x+273.15), 2))}')
except ValueError:
    print('Not a number!')
except Exception:
    print('237.15 is the absolute minimum of themperature in degrees, ypu can\'y have less than that!')