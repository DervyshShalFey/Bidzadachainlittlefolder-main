from transformation import *
from math import *
try:
    x = float(input('Insert first number: '))
    x = transform(x)
    y = float(input('Insert second number: '))
    y = transform(y)
    z = float(input('Insert third number: '))
    z = transform(z)
    print(f'A) a = (e+(f/2))/3  \n   If e is equal to {x} and f is equal to {y}, then x will be equal to {transform((x+(y/2))/3)}')
    print(f'Б) b = |h^2 - g|\n   If g is equal to {z} and h is equal to {y}, then b will be equal to {transform(module((y**2)-z))}')
    try:
        print(f'B) c = √(((g - h)^2)-3 * sinus of e)\n   If e is equal to {x}, h is equal to {y} and g is equal to {z}, then x will be equal to {sqrt(((z-y)**2)-3*sin(x))}')
    except:
        print(f'B) Square root of (({z}{tpluey(y)})^2)-3*sinus of {x}')
except ValueError:
    print('Not a number!')