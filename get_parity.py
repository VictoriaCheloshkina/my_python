x = int(input('Введите число: '))
def parity(x):
    if x%2 == 0:
        return 'Четное'
    else:
        return 'Нечетное'
print(parity(x))
