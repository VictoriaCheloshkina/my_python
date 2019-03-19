def calc(expr):
    '''
    >>> calc("1 2 + 4 * 3 +")
    '15'
    >>> calc("1 2 3 * + 2 -")
    '5'
    '''
    list1 = []
    for i in expr:
        if i.isdigit():
            list1.append(int(i))
        elif i == '+':
            a = list1.pop()
            b = list1.pop()
            list1.append(int(a)+int(b))
        elif i == '-':
            a = list1.pop()
            b = list1.pop()
            list1.append(int(b)-int(a))
        elif i == '*':
            a = list1.pop()
            b = list1.pop()
            list1.append(int(a)*int(b))
    return str(list1[0])

print(calc("1 2 3 * + 2 -"))

import doctest
doctest.testmod()
