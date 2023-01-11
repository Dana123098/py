print("rozmir tablicy (do 10) Wpisz 0 dla zakonczenia: ")
list=[]
i=0
d=1
while d!=0 and i<10:
    m=int(input("podaj wartości: "))
    list.append(m)
    i+=1
    d=m
print(list)
for i in list:
    if i % 2 == 0:
        list.sort(key=lambda i:(i%2, not i%2))
print(list)

#  Po zakończonym wczytywaniu ustawić liczby tak, aby liczby
# parzyste znalazły się po jednej stronie tablicy, a nieparzyste po drugiej.
