from transformation import *
try:
    x = float(input('Insert a number: '))
    x = transform(x)
    print(f'A) y = 7(x^2) - 3x + 6 \n   If x is equal to {x}, then y will be equal to {transform(7*(x**2)-3*x+6)}')
    print(f'Б) x = 12(a^2) + 7a - 16 \n   If a is equal to {x}, then x will be equal to {transform(12*(x**2)+7*x-16)}')
except ValueError:
    print('Not a number!')