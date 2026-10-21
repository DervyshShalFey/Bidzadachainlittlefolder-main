from math import *
from transformation import *

try:
    x = float(input('Insert 1st number: '))
    x = transform(x)
    y = float(input('Insert 2nd number: '))
    y = transform(y)
    z = float(input('Insert 3rd number: '))
    z = transform(z)
    try:
        print(f'A) -1 / {neg(x)}^2 = {transform(-1/x**2)}')
    except:
         print('A) Can\'t divide by zero!')
    try:
        print(f'Б) {x}/{neg(y)}*{neg(z)} = {transform(x/(y*z))}')
    except: 
         print('Б) Can\'t divide by zero!')
    try:
        print(f'B) {z}*{neg(x)}/{neg(y)} = {transform(z*(x/y))}')
    except:
         print('В) Can\'t divide by zero!')
    print(f'Г) ({x}{pluey(y)})/2 = {transform((x+y)/2)}')
    try:
        print(f'Д) 5.45 * ({x} + 2 * {neg(y)})/(2 - {x}) = {transform(5.45*(x+2*y)/(2-x))}')
    except:
         print('Д) Can\'t divide by zero!')
    try:
        print(f'E) ({tpluey(y)}+√{neg(y)}^2-4*{neg(x)}*{neg(z)})/(2*{neg(x)}) = {transform((-y+sqrt(y**2-4*x*z))/(2*x))}')
    except ValueError:
            print(f'Е) Square root of {neg(y)}-4*{neg(x)}*{neg(z)} is undefined')
    except ZeroDivisionError:
         print('Е) Can\'t divide by zero!')
    try:
         print(f'Ж) ({tpluey(y)} + (1 / {neg(x)}))/(2/{neg(z)}) = {(transform(-y + (1/x))/(2/z))}')
    except:
         print('Ж) Can\'t divide by zero!')
    try:
         print(f'3) 1/(1+({x}{pluey(y)})/2) = {transform(1/1+(x+y)/2)}')
    except:
         print('3) Can\'t divide by zero!')
    print(f'И) 1/(1/(2/(1/(2/(3/5))))) = {1/(1/(2/(1/(2/(3/5)))))}')
    print(f'((2)^{neg(x)})^{neg(y)} = {transform(((2)**x)**y)})')
except ValueError:
    print('Not a number!')