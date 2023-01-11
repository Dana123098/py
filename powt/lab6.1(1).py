n=int(input("podaj rozmiar tablicy 4 liczdy:"))
list=[]
list2=[]
list3=[]
i=0
while i<n:
    m=int(input("Podaj liczby: "))
    list.append(m)
    i+=1
print(list)

ost=list[-1]
list.pop(list.index(list[-1]))
for i in list:
    i=i/ost
    list2.append(i)
print("Liczby pod. przez ostatnią liczbe: ")
print(list2)

for i in list2:
    kw=i**2
    list3.append(kw)

print("Kwad:",list3)
print("Sum:", sum(list3))


