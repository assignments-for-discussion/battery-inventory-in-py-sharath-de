def count(a):
    low=[]
    med=[]
    high=[]
    for i in range(len(a)):
        if a[i]<400:
            low.append(a[i])
        elif a[i]>400 and a[i]<919:
            med.append(a[i])
        else:
            high.append(a[i])
    l=[low,len(low)]
    m=[med,len(med)]
    h=[high,len(high)]
    return l,m,h
a=[100, 300, 500, 600, 900, 1000]
print(count(a))
