# 3. Pobrać od użytkownika rozmiar tablicy n, a następnie wczytać n podanych przez
# użytkownika liczb całkowitych do tablicy. Odnaleźć liczby, których suma cyfr jest
# większa od ostatniego elementu podanego przez użytkownika. Znalezione liczby
# umieścić w drugiej tablicy. Przed wyjściem z programu wyświetlić ich ilość.

n=int(input("Rozmiar n="))
i=0
list=[]
list2=[]
list_sm = []

while i<n:
    d=int(input("liczby d="))
    list.append(d)
    i+=1
print(list)
# //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
end=list[-1]

for i in list:
    list_sm.append(sum(map(int, str(i))))
print(list_sm)

for i in list_sm:
    if i > end:
        list2.append(i)
        print(i)
        print(list2)