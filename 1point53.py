from transformation import *
from math import *
try:
    x2 = float(input('Cost of system unit in $: '))
    if x2 <= 0:
        raise Exception
    x2 = transform(x2)

    y2 = float(input('Cost of keyboard in $: '))
    if y2 <= 0:
        raise Exception
    y2 = transform(y2)

    z2 = float(input('Cost of mouse in $: '))
    if z2 <= 0:
        raise Exception
    z2 = transform(z2)
    print(f'If we buy 3 computers this way, we will pay {(x2+y2+z2)*3}')

    x = float(input('Number of computers you buy: '))
    if x <= 0:
        raise Exception
    if x == int(x):
        x = int(x)
        print(f'You must pay {transform((x2+y2+z2)*x)}$ to buy {x} computers!')
    else:
        print(f'You can\'t buy {x} computers!')
    

except ValueError:
    print('Not a number!')
except Exception:
    print('Number can\'t be negative or be equal to zero!')