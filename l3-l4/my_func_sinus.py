from math import sin
a=float(input('Введите вещественное число: '))
def fun1(a):
    if 0.2 <= a <= 0.9:
        return sin(a)
    else:
        return 1
print(fun1(a))

