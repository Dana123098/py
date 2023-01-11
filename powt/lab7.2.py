a = int(input("Ile chczesz liczb: "))
list = []
i=0
d=0
while i < a:
    m = int(input("Wprowadz liczby: "))
    list.append(m)
    i+=1
print(list)
for  d in list:
    while (len(list))==a:
        n=int(input("podaj element dla usun.:"))
        list.pop(list.index(n))
    
print(list)
print("Sum: ", sum(list))

list_sm = []
for i in list:
    list_sm.append(sum(map(int, str(i))))
print("Sum tab:",list_sm)