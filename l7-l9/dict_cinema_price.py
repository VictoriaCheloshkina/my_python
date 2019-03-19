movies = {"Пятница": {'12': 250, '16': 350, '20': 450},
          "Чемпионы": {'10': 250, '13': 350, '16': 350},
          "Пернатая банда": {'10': 350, '14': 450, '18': 450}}
movie = input('Введите название фильма: ')
date = input('Введите дату (сегодня, завтра): ') 
time = input('Введите время: ')
tickets = int(input('Введите количество билетов: ')) 
def discount1(date):
    if date == "сегодня":
        return 0
    elif date == "завтра":
        return 0.05

def discount2(tickets):
    if tickets < 20:
        return 0
    else:
        return 0.20

def price(movie, tickets, date, time):
    return tickets*movie[time] - tickets*movie[time]*(discount1(date) + discount2(tickets))
if movie in movies:
    if date == "сегодня" or date == "завтра":
        if time in movies[movie]:
            print("Выбрали фильм:", movie, "День:", date, "Время:", time, "Количество билетов:", tickets)
            print("Итого:", price(movies[movie], tickets, date, time))
        else:
            print("Неправильно указано время")
    else:
        print("Неправильно указан день")
else:
    print("Неправильно указан фильм")
