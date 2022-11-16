n = int(input("Wproadz ile chzcesz liczb:"))
list1 = []
i = 0
while i < n:
    m = int(input("Wprowadz liczy: "))
    list1.append(m)
    i+=1
print(list1)

for i in list1:
    list2 = [list1[:-1]**2]
    
    print(list2)
    