def calc(first, second, operator):
    if operator == "+":
        return first+second
    if operator == "-":
        return first - second
    if operator == "*":
        return first*second
    if operator == "/":
        return first/second
    else:
        raise ValueError

while True:
    try:
        first = float(input("Введите первое число: "))
        second = float(input("Введите второе число: "))
        operator = input("Введите оператор: ")
        print("Результат:", calc(first, second, operator))
        break
    except ZeroDivisionError:
        print("Ошибка деления на ноль, попробуйте еще раз")
    except ValueError as err:
        print("Ошибка ввода, попробуйте еще раз")

