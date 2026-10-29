x = input('Insert anything to exchange(x): ')
y = input('Insert anything to exchange(y): ')
print(f'Before exchange: x = {x}, y = {y}')
temp = x
x = y
y = temp
print(f'After exchange: x = {x}, y = {y}')