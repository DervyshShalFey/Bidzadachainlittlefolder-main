from transformation import *
try:
    x = int(input('Insert 1st whole number: '))
    y = int(input('Insert 2nd whole number: '))
    z = int(input('Insert 3rd whole number: '))
    a = int(input('Insert 4th whole number: '))
    x = transform(x)
    y = transform(y)
    z = transform(z)
    a = transform(a)
    print(x)
    print(y)
    print(z)
    print(a)
except:
    print('Not a whole number')