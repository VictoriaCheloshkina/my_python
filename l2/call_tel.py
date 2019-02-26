x = int(input('Введите код города: '))
y = int(input('Введите длительность переговоров: '))
def call(x,y):
    if x == 343:
        return y*15 
    elif x == 381:
        return y*18
    elif x == 473:
        return y*13
    elif x == 485:
        return y*11
    else:
        return 'Ошибка. Введен неизвестный код города'
print('Стоимость в рублях:',call(x,y))
