list1 = []
import json

def writer(filename, numbers): 
    try:
        with open(filename, 'w') as f_obj:
            json.dump(numbers, f_obj)
    except Exception as e:
        print(e)

while True:
    number = int(input(
        'Простой todo:\n 1. Добавить задачу.\n 2. Вывести список задач.\n 3. Выход.\nУкажите число: '))    
    if number == 1:
        newlist = {}
        newlist['name'] = input('Сформулируйте задачу: ')
        newlist['category'] = input('Добавьте категорию к задаче: ')
        newlist['time'] = input('Добавьте время к задаче: ')
        list1.append(newlist)
    if number == 2:
        for i in list1:
            for j in i:
                print(j,':',i[j],end=' ')
            print()
    if number == 3:
        writer('todo.json', list1)
        print('Файл сохранен')
        break
    
