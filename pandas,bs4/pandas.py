import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
data = pd.read_csv('opendata.csv', encoding='cp1251')
data.head()
data1 = data[data['name'] == 'Средняя зарплата'][data['region'] == 'Санкт-Петербург']
sredzn = data1.value.mean()
naib = data1.value.max()
naim = data1.value.min()
data2 = data[data['name'] == 'Средняя пенсия'][data['region'] == 'Санкт-Петербург']
sredznp = data2.value.mean()
naibp = data2.value.max()
naimp = data2.value.min()
print(sredzn, '-средняя зарплата \n', naib,'- максимальная зарплата \n',naim,'- максимальная зарплата \n',sredznp, '-средняя пенсия \n', naibp,'- максимальная пенсия \n',naimp,'- максимальная пенсия \n')
dataplot = data1[["date", "value"]]
dataplot.head()
dataplot[:20].plot.line()
