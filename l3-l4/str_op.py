s="У лукоморья 123 дуб зеленый 456"
if s.find('я')!=-1:
    print(s.index('я'))
print((s.lower()).count('у'))
if s.isalpha() == False:
    print(s.upper())
if len(s) >= 4:
    print(s.lower())
s = 'О' + s[1:]
print(s)
