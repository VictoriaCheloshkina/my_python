from math import pi
a=int(input('Введите число: '))
def fun1(a):
    return f'{pi:.{a}f}'
print(fun1(a))
