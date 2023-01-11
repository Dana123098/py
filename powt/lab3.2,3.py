# wynik=0
# wynik2=0
# while wynik<=255 and wynik2<=50000:
#     a = int(input("Podaj liczby: "))
#     wynik+=a
#     wynik2*=a
# print()


# Wczytywać liczby od użytkownika do momentu, gdy ich suma przekroczy 255 lub
# iloczyn będzie większy od 50000, a następnie wyświetlić ich średnią arytmetyczną.
sum=0
m=1
while sum<255 and m<50000:
    a=int(input("Podaj liczbe:"))
    sum+=a
    m*=a
print(sum, m)