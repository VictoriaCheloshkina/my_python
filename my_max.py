x = int(input('Введите x: '))
y = int(input('Введите y: '))
def max(x,y):
    if x > y:
        return x
    else:
        return y
print('Наибольшее число: ',max(x,y))
