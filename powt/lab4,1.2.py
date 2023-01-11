# 2. Wczytać od użytkownika n wartości. Po uzupełnieniu tablicy pobrać dwie wartości
# określające obszar poszukiwań – sprawdzić i wypisać ile elementów tablicy mieści się
# w wyznaczonym przedziale.
n=int(input("podaj liczby: "))
list=[]
list2=[]
i=0
while i<n:
    m=int(input("podaj liczby:"))
    list.append(m)
    i+=1
print(list)
d=int(input("Podaj 1 liczbu określającu obszr poszukiwań:"))
b=int(input("Podaj 2 liczbu określającu obszr poszukiwań:"))
for i in list:
    if d<=i and b>=i:
        list2.append(i)
print(list2)
print(len(list2))
/

