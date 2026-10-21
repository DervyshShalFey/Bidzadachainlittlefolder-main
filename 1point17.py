from math import *
from transformation import *
try:
    x = float(input('Insert 1st number: '))
    x = transform(x)
    y = float(input('Insert 2nd number: '))
    y = transform(y)
    z = float(input('Insert 3rd number: '))
    z = transform(z)
    a = float(input('Insert 4th number: '))
    a = transform(a)
    print(f'A) √{neg(x)}^2+{neg(y)}^2 = {transform(sqrt((x**2)+(y**2)))}')
    print(f'Б) {x}*{neg(y)}{pluey(x)}*{neg(z)}{pluey(y)}*{neg(z)} = {transform(x*y+x*z+y*z)}')
    print(f'B) {x}*{neg(y)}+(({z}*{neg(y)}^2)/2) = {transform(x*y+((z*(y**2))/2))}')
    print(f'Г) (({x}*{neg(y)}^2)/2){pluey(x)}*9.8*{neg(z)} = {transform(((x*(y**2))/2)+x*9.8*z)}')
    try:
        print(f'Д) 1/{neg(x)}+1/{neg(y)} = {transform(1/x+1/y)}')
    except:
        print('Д) Can\'t divide by zero!')
    print(f'E) {x}*9.8*cosinus of {y} = {x*9.8*cos(y)}')
    print(f'Ж) 2*3.14*{neg(x)} = {transform(2*3.14*x)}')
    print(f'3) {neg(y)}^2-4*{neg(x)}*{neg(z)} = {transform(y**2-4*x*z)}')
    try:
        print(f'И) {a}*(({x}*{neg(y)})/{neg(z)}^2) = {a*((x*y)/(z**2))}')
    except:
        print('И) Can\'t divide by zero!')
    print(f'K) {neg(y)}^2*{neg(x)} = {transform((y**2)*x)}')
    print(f'Л) {x}*{neg(y)}*sinus of {z} = {transform(x*y*sin(z))}')
    try:
        print(f'M) √{neg(x)}^2+{neg(y)}^2-2*{neg(x)}*{neg(y)}*cosinus of {z} = {sqrt((x**2)+(y**2)*cos(z))}')
    except:
        print(f'M) Square root of {neg(x)}^2+{neg(y)}^2-2*{neg(x)}*{neg(y)}*cosinus of {z} is undefined')
    print(f'Н) ({x}*{neg(a)}{pluey(y)}*{neg(z)})/{neg(x)}*{neg(a)} = {transform((x*a+y*z)/x*a)}')
    try:
        print(f'O) √1-square of sinus of {x} = {sqrt(1-sin(x)**2)}')
    except:
        print(f'O) Square root of 1-square of sinus of {x} is undefined')
    try:
        print(f'П) 1/(√{neg(x)}*{neg(a)}^2{pluey(y)}*{neg(a)}{pluey(z)}) = {transform(1/(sqrt(x*(a**2)+y*a+z)))}')
    except ZeroDivisionError:
        print('П) Can\'t divide by zero!')
    except:
        print(f'П) Square root of {neg(x)}*{neg(a)}^2{pluey(y)}*{neg(a)}{pluey(z)} is undefined')
    try:
        sqrt(x)
        try:
            sqrt(x+1)
            try:
                sqrt(x-1)
                try:
                    print(f'P) ((√{neg(x)}+1)+(√{neg(x)}-1))/2*√{neg(x)} = {transform(((sqrt(x+1))+(sqrt(x-1))/2*sqrt(x)))}')
                except:
                    print(f'P) Can\'t divide by zero!')
            except:
                print(f'P) Square root of {x}-1 is undefined')
        except:
            print(f'P) Square root of {x}+1 is undefined')
    except:
        print(f'P) Square root of {x} is undefined')
    print(f'C) |{x}|+|{x}+1| = {transform(module(x)+module(x+1))}')
    print(f'T) |1-|x|| = {transform(module(1-module(x)))}')
except ValueError:
    print('Not a number!')