def transform(x): # превращение целых чисел в инт
    if x.is_integer():
        x = int(x)
    return x
def neg(x): #добавление скобок отрицательным числам после * или /
    if x < 0:
        x = str(x)
        x = f'({x})'
    return x
def pluey(x): #добавление при +
    if x >= 0:
        x = str(x)
        x = f'+{x}'
    return x
def tpluey(x): #добавление при -
    x*=-1
    if x > 0:
        x=str(x)
        x=f'+{x}'
    return x

def module(x): # Просто модуль типо |x|
    if x < 0:
        x*=-1
    return x