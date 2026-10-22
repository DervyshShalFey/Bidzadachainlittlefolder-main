from transformation import *
try:
    x = float(input('Insert first number: '))
    x = transform(x)
    y = float(input('Insert second number: '))
    y = transform(y)
    print(f'Sum: {transform(x+y)}')
    print(f'Subtraction: {transform(x-y)}')
    print(f'Product: {transform(x+y)}')
    try:
        print(f'Division: {transform(x/y)}')
    except ZeroDivisionError:
        print('Division: Can\'t divide by zero!')
except ValueError:
    print('Not a number!')