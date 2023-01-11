n=int(input("podaj ilość ocen:"))
list=[]
list2=[]
i=0
s=0
while i<n:
    m=int(input("Podaj oceny: "))
    list.append(m)
    i+=1
print("Oceny:", list)

for i in list:
    if i>2:
        print("Zlicony")
    else:
        print("Nie zal.")


def oblicz_srednia():
    s=(sum(list)/n)
    print(s)


    for i in list:
        if i>s:
            list.sort(key=lambda i:(i>s and i>s))
    print(list)


oblicz_srednia()

