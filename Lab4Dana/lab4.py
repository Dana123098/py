#4.1
# n = int (input("Podaj dlugość tablicy:"))
# tab = [0]*n
# i=0
# while i<n:
#     tab[i] = int(input("Wprowadz liczbe do tabeli:"))
#     i +=1
# print(tab)
# print("Max:", max(tab))
# print("Min:", min(tab))

#4.2

# n = int(input("Podaj dlugość tablicy:"))
# list1 = []
# list2 = []
# i=0
# while i<n:
#     m=int(input("Poda liczba"))
#     list1.append(m)
#     i+=1

# print(list1)
# a = int(input("Podaj lewyj przedział:"))
# b = int(input("Podaj prawy przedział:"))
# for i in list1:
#     if a <= i and b >= i:
#         list2.append(i)
# print(list2)
         


# print("Podaj i wyszukaj element w liczbe:")
# e = int(input("Liczba:"))
# print(tab.count(e))


#4.4
# n = int(input("Podaj dlugość tablicy:"))
# tab = [0]*n
# i=0
# while i<n:
#     tab[i] = int(input("Wprowadz liczbe do tabeli:"))
#     i+=1
# print(tab)
# print(*list(set([e for e in tab if tab.count(e)>2])))


#4.5
n = int (input("Podaj dlugość tablicy:"))
if n < 4:
    print("Podaj nie < 4 liczb")
tab = [0]*n
i=0
while i<n:
    tab[i] = int(input("Wprowadz liczbe do tabeli:"))
    i +=1
print(tab)
