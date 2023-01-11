# Pobierać od użytkownika wartości do momentu wpisania wartości zero. Znaleźć i
# wypisać wszystkie elementy, które pojawiły się w tablicy więcej niż dwa razy
print("Wpisz 0 dla zakonczenia")
list=[]
i=1
d=0
while i!=0:
    m=int(input("podaj liczby:"))
    list.append(m)
    i=m
list.pop(-1)
print(list)
# !!!!!!!!!!!!!!!!!!!!!
for d in list:
    if list.count(d)>2:
        print(d)
/