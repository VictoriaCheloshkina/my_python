def read_url(url):
    import urllib.request
    try:
        with urllib.request.urlopen(url) as webpage:
            text = webpage.read().decode('utf-8')
        return text
    except Exception as e: 
        return e
    
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

if __name__ == "__main__":    
    text = read_url("http://dfedorov.spb.ru/python3/src/romeo.txt")
    print(text)
    print(histogram(text.split()))
