x=['самовар','весна','лето']
import random
a=random.choice(x)
b=random.randint(0,len(a)-1)
d=a[:b]+'?'+a[b+1:]
print(d)
c=input('Введите букву: ')
if a[b]==c:
    print('Победа!')
else:
    print('Увы. Попробуйте в другой раз.')
print('Слово: ',a)
