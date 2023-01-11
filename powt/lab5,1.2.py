# . Pobrać od użytkownika rozmiar tablicy n, a następnie wczytać n podanych przez
# użytkownika wartości do tablicy. Obliczyć i wyświetlić sumę oraz średnią wszystkich
# elementów większych od ostatniego. Przygotować diagram NS oraz zaimplementować
# algorytm w języku Python.
n=int(input("Podaj rozmiar tablicy:"))
list=[]
list2=[]
i=0
sum=0
sr=0
while i<n:
    m=int(input("Podaj liczbu:"))
    list.append(m)
    i+=1
print(list)
print("Ostatni:",list[-1])
for i in list:
    if i>list[-1]:
        list2.append(i)
print(list2)
for i in list2:
    sum=sum+i
    sr=sum/(len(list2))
print("Suma:", sum, "Średnia:", sr)
