x = input('Введите название фильма: ')
y = input('Введите дату (сегодня, завтра): ')
z = int(input('Введите время: '))
w = int(input('Введите количество билетов: '))
print('Выбрали фильм: ',x, 'День: ',y,'Время: ',z,'Количество билетов: ',w)
if x == 'Пятница':
    if y == 'сегодня':
        if z == 12:
            if w >= 20:
                print('Стоимость: ',w*250*0.8)
            else:              
                print('Стоимость: ',w*250)
        elif z == 16:
             if w >= 20:
                print('Стоимость: ',w*350*0.8)
             else:
                print('Стоимость: ',w*350)
        elif z == 20:
             if w >= 20:
                print('Стоимость: ',w*350*0.8)
             else:
                print('Стоимость: ',w*350)
        else:
                print('Ошибка ввода')
    if y == 'завтра':
         if z == 12:
             if w >= 20:
                 print('Стоимость: ',w*250*0.75)
             else:
                 print('Стоимость: ',w*250*0.95)
         elif z == 16:
             if w >= 20:
                 print('Стоимость: ',w*350*0.75)
             else:          
                print('Стоимость: ',w*350*0.95)
         elif z == 20:
             if w >= 20:
                print('Стоимость: ',w*350*0.8)
             else:
                print('Стоимость: ',w*350)
         else:
                print('Ошибка ввода') 
elif x == 'Чемпионы':
    if y == 'сегодня':
        if z == 10:
            if w >= 20:
                print('Стоимость: ',w*250*0.8)
            else:              
                print('Стоимость: ',w*250)
        elif z == 13:
             if w >= 20:
                print('Стоимость: ',w*350*0.8)
             else:
                print('Стоимость: ',w*350)
        elif z == 16:
             if w >= 20:
                print('Стоимость: ',w*350*0.8)
             else:
                print('Стоимость: ',w*350)
        else:
                print('Ошибка ввода') 
    if y == 'завтра':
         if z == 10:
             if w >= 20:
                 print('Стоимость: ',w*250*0.75)
             else:
                 print('Стоимость: ',w*250*0.95)
         elif z == 13:
             if w >= 20:
                 print('Стоимость: ',w*350*0.75)
             else:          
                print('Стоимость: ',w*350*0.95)
         elif z == 16:
             if w >= 20:
                print('Стоимость: ',w*350*0.8)
             else:
                print('Стоимость: ',w*350)
         else:
                print('Ошибка ввода')
elif x == 'Пернатая банда':
    if y == 'сегодня':
        if z == 10:
            if w >= 20:
                print('Стоимость: ',w*350*0.8)
            else:              
                print('Стоимость: ',w*350)
        elif z == 14:
             if w >= 20:
                print('Стоимость: ',w*450*0.8)
             else:
                print('Стоимость: ',w*450)
        elif z == 18:
             if w >= 20:
                print('Стоимость: ',w*450*0.8)
             else:
                print('Стоимость: ',w*450)
        else:
                print('Ошибка ввода') 
    if y == 'завтра':
         if z == 10:
             if w >= 20:
                 print('Стоимость: ',w*350*0.75)
             else:
                 print('Стоимость: ',w*350*0.95)
         elif z == 14:
             if w >= 20:
                 print('Стоимость: ',w*450*0.75)
             else:          
                print('Стоимость: ',w*450*0.95)
         elif z == 18:
             if w >= 20:
                print('Стоимость: ',w*450*0.8)
             else:
                print('Стоимость: ',w*450)
         else:
                print('Ошибка ввода')
else:
    print('Ошибка ввода')
