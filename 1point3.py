from transformation import *
try:
    x = float(input('Insert number: '))
    x = transform(x)
    print('You\'ve inserted number')
except ValueError:
    print('You\'ve inserted not a number')