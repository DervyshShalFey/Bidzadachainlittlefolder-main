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
    b = float(input('Insert 5th number: '))
    b = transform(b)
    try:
        print(f'A) {x}/{neg(y)}/{neg(z)} = {transform(x/y/z)}')
    except:
         print('A) Can\'t divide by zero!')
    try:
        print(f'Б) {x}*{neg(y)}/{neg(z)} = {transform(x*y/z)}')
    except:
        print('Б) Can\'t divide by zero!')
    try:
        print(f'B) {x}/{neg(y)}*{neg(z)} = {transform(x/(y*z))}')
    except:
        print('B) Can\'t divide by zero!')
    try:
        print(f'Г) ({x}{pluey(y)})/{neg(z)} = {transform((x+y)/z)}')
    except:
        print('Г) Can\'t divide by zero!')
    try:
        print(f'Д) {x}+({y}/{neg(z)}) = {transform(x+(y/z))}')
    except:
        print('Д) Can\'t divide by zero!')
    try:
        print(f'E) ({x}{pluey(y)})/({y}{pluey(z)}) = {transform((x+y)/(y+z))}')
    except:
        print('E) Can\'t divide by zero!')
    try:
        print(f'З) {x}/sinus of {y} = {x/sin(y)}')
    except:
        print('З) Can\'t divide by zero!')
    try:
        print(f'И) 1/(2*{neg(x)}*{neg(y)}*sinus of {z}) = {1/(2*x*y*sin(z))}')
    except:
         print('И) Can\'t divide by zero!')
    try:
        print(f'K) (2*{neg(y)}*{neg(z)}*cosinus of {x}/2)/({y}{pluey(z)}) = {(2*y*z*cos(x/2))/(y+z)}')
    except:
         print('K) Can\'t divide by zero!')
    print(f'Л) 4*{neg(a)}*((sinus of {x})/2)*((sinus of {y})/2)*((sinus of {z})/2) = {4*a*(sin(x)/2)*(sin(y)/2)*(sin(z)/2)}')
    try:
        print(f'М) ({x}*{neg(a)}{pluey(y)})/({z}*{neg(a)}{pluey(b)}) = {transform((x*a+y)/(z*a+b))}') 
    except:
        print('M) Can\'t divide by zero!')
    print(f'H) 2*sinus of ({x}{pluey(y)})/2*cosinus of ({x}{tpluey(y)})/2 = {2*sin((x+y)/2)*cos((x-y)/2)}')
    print(f'O) Absolute value of (2*sinus of (-3*absolute value of ({x}/2))) = {module(2*sin(-3*module(x/2)))}')
except ValueError:
    print('Not a number!')