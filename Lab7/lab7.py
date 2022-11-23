#7.1
a = int(input("Ile masz egzaminów: "))
list = []
i=0
while i < a:
    m = int(input("Napisz oceny: "))
    list.append(m)
    i+=1
print(list)
for i in list:
    if  i > 2:
        print("Zaliczony")
    else:
        print("Nie zaliczony")
s=(sum(list)/a)
def oblicz_srednia():
    
    print(s)
oblicz_srednia()

for i in list:
    if i > s:
        list.sort(key=lambda i:(i>s, not i>s))
print(list)  