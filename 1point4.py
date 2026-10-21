from transformation import *
try:
    x = float(input('Insert number: '))
    x = transform(x)
    print(f'{x} is the number you\'ve inserted')
except ValueError:
    print('You\'ve inserted not a number')