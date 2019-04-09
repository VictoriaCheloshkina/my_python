try:
    with open('temper.stat', 'r') as r, open('temper.result', 'w') as w:
        temper =list(map(lambda x: float(x.strip()), r.readlines()))
        w.write("Максимальная температура: ", str(max(temper)), "\n")
        w.write("Минимальная температура: ", str(min(temper)), "\n")
        w.write("Средняя температура: ", str(sum(temps)/len(temper)), "\n")
        w.write("Количество уникальных температур: ", str(len(set(temper))))
except Exception as err:
    print(err)
