a=[2,4,9,16,25]

forlist=[]
for i in a:
    forlist.append(i**(1/2))
print(forlist)

maplist=list(map((lambda x:x**(1/2)),a))
print(maplist)

genlist=[i**(1/2) for i in a]
print(genlist)

