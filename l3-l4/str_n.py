s = input('Введите строку: ')
n = int(input('Введите число: '))
def fun1(s,n):
    if len(s) > n:
        return s.upper()
    else:
        return s
print(fun1(s,n))
