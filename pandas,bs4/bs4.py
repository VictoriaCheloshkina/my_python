import bs4
def read_url(url):
    import urllib.request    
    with urllib.request.urlopen(url) as webpage:
        text = webpage.read().decode('utf-8')
    return text
text = read_url("http://dfedorov.spb.ru/python3/forecast.html")
special_list = bs.select('.forecast-label')
weekday = [special_list[0].text,special_list[1].text,special_list[2].text,special_list[3].text,special_list[4].text,special_list[5].text,special_list[6].text,special_list[7].text,special_list[8].text,special_list[9].text,special_list[10].text,special_list[11].text,special_list[12].text]
special_list2 = bs.select('.forecast-text')
weather = [special_list[0].text,special_list2[1].text,special_list2[2].text,special_list2[3].text,special_list2[4].text,special_list2[5].text,special_list2[6].text,special_list2[7].text,special_list2[8].text,special_list2[9].text,special_list2[10].text,special_list2[11].text,special_list2[12].text]
with open('res.csv', 'w') as f:
    wr = csv.writer(f, delimiter=' ')
    wr.writerows([(weekday[i], weather[i]) for i in range(len(weekday))])
