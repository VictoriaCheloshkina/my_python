from random import randint
a=randint(0,4)
b=int(input())
if a==b:
    print('Победа')
else:
    print('Повторите ещё раз!')
    if a>b:
        print('Результат больше')
    else:
        print('Результат меньше')
   
