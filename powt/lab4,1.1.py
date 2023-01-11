n = int(input("podaj ile hcesz liczb"))
list=[]
i=0

while i<n:
    m=int(input("podaj liczby:"))
    list.append(m)
    i+=1
print("List1:", list)
max1=max(list)
print("Max1:", max1)

# list2=[]
list.pop(list.index(max(list)))
# for i in list:
#     list2.append(i)
# print(list2)

max2=max(list)

print("Max2: ", max2)
