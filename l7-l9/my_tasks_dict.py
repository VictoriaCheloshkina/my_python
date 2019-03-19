list1 = []
while True:
    number = int(input(
        'Простой todo:\n 1. Добавить задачу.\n 2. Вывести список задач.\n 3. Выход.\nУкажите число: '))    
    if number == 1:
        newlist = {}
        newlist['Задача'] = input('Сформулируйте задачу: ')
        newlist['Категория'] = input('Добавьте категорию к задаче: ')
        newlist['Время'] = input('Добавьте время к задаче: ')
        list1.append(newlist)
    if number == 2:
        for i in list1:
            for j in i:
                print(j,':',i[j],end=' ')
            print()
    if number == 3:
        break
