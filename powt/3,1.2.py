#  Wczytać w pętli n liczb z przedziału od 10 do 50 (wartość n pobrać od użytkownika
# przed wejściem do pętli), a następnie wyświetlić sumę ich kwadratów.
n = int(input("Podaj ile chcesz liczb:"))
list=[]
i=0
x=0
while i<n:
    m=int(input("Podaj liczby od 10 do 50: "))
    list.append(m)
    i+=1
print(list)
b=[x**2 for x in list]
# for x in list:
#     b=x**2
#     x
print("KK: ", b)

print("Sum:", sum(b))
/