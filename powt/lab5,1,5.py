n = int(input("podaj ile hcesz liczb"))
list=[]
i=0

while i<n:
    m=int(input("podaj liczby:"))
    list.append(m)
    i+=1
print("List1:", list)

for i in list:
    if i%5==0:
        list.pop(list.index(i))
print(list)