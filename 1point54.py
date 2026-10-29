import pprint

from transformation import *
from math import *
try:
    x = float(input('Insert Tanya\'s age: '))
    x = transform(x)
    if x < 0:
        raise Exception
    if x == int(x):
        y = float(input('Insert Mitya\'s age: '))
        y = transform(y)
        if y < 0:
            raise Exception
        
        l = [x, y]
        if y == int(y):
            z = transform((x+y)/2)
            
            print(f'Average age of theirs: {z}')
            for i in l:
                if i == x:
                    b = "Tanya"
                elif i == y:
                    b = "Mitya"
                if z-i != 0:
                    if z-i > 0:
                        a = 'older'
                    else:
                        a = 'younger'
                    print(f'{b} is {module(z-i)} years {a} than their average age')
                else:
                    if i<18:
                        print('Both kids\' age is equal to their average, so they are the same age!')
                    else:
                        print('Both adults\' age is equal to their average, so they are the same age!')
                    break
                    
        else:
            print('Age must be a whole number!')
    else:
        print('Age must be a whole number!')

    

except ValueError:
    print('Not a number!')
except Exception:
    print('Number can\'t be negative!')