from transformation import *
try:
    x = float(input('Insert first number: '))
    x = transform(x)
    y = float(input('Insert second number: '))
    y = transform(y)
    print(f'A) z = x^3 - 2.5xy + 1.78x^2 - 2.5y + 1 \n   If x is equal to {x} and y is equal to {y}, then z will be equal to {transform((x**3)-2.5*x*y+1.78*(x**2)-2.5*y+1)}')
    print(f'Б) x = 3.56a + b^3 - 5.8b^2 + 3.8a - 1.5 \n   If a is equal to {x} and b is equal to {y}, then x will be equal to {transform(3.56*x+(y**3)-5.8*(y**2)+3.8*x-1.5)}')
except ValueError:
    print('Not a number!')