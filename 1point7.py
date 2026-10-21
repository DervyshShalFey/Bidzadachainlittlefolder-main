from transformation import *
try:
    x = float(input('Insert 1st number: '))
    y = float(input('Insert 2nd number: '))
    z = float(input('Insert 3rd number: '))
    x = transform(x)
    y = transform(y)
    z = transform(z)
    print(x, end='  ')
    print(y, end='  ')
    print(z, end='  ')
except ValueError:
    print('Not a number')