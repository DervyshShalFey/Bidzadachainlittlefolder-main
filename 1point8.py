from transformation import *
try:
    x = float(input('Insert 1st number: '))
    y = float(input('Insert 2nd number: '))
    z = float(input('Insert 3rd number: '))
    a = float(input('Insert 4th number: '))
    x = transform(x)
    y = transform(y)
    z = transform(z)
    a = transform(a)
    print(x, end=' ')
    print(y, end=' ')
    print(z, end=' ')
    print(a, end=' ')
except:
    print('Not a whole number')