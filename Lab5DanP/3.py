n = int(input("Wproadz ile chzcesz liczb:"))
list1 = []

i = 0
while i < n:
    m = int(input("Wprowadz liczy: "))
    list1.append(m)
    i+=1
print(list1)
ost=list1[-1]
print(ost)

list2 = list1[:-1]
print(list2)

sum = 0
for  i in list2:
    sum+=i
    print("sum: ", sum)
if sum >= ost:
    print("Ostatni - sum:", ost - sum)
else:
    print("ostatni > sum")
