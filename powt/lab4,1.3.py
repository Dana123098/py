
# ????????????????????????????????//
# Uwzględnić zarówno tablice o
# parzystej, jak i nieparzystej liczbie elementów.

print("Wpisz 0 dla zakonczenia")
list=[]
i=1
while i>0:
    m=int(input("podaj liczby:"))
    list.append(m)
    i=m
list.pop(-1)
print(list)
s=[d%2==0 for d in list]
print(s)
/
/
/