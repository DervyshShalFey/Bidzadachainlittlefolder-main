a = input('Insert anything to exchange(a): ')
b = input('Insert anything to exchange(b): ')
c = input('Insert anything to exchange(c): ')
print(f'Before exchange: a = {a}, b = {b}, c = {c}')
temp = a
a = b
b = c
c = temp
print(f'After exchange(a): a = {a}, b = {b}, c = {c}')
temp = a
a = b
b = c
c = temp
print(f'After exchange(б): a = {a}, b = {b}, c = {c}')