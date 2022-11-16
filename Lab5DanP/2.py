#5.2
n = int(input("Wproadz ile chzcesz liczb:"))
list = []
i = 0
while i < n:
    m = int(input("Wprowadz liczy: "))
    list.append(m)
    i+=1
print(list)
for i in list:
    if i < list[len(list)-1]:
        list.remove(i)
        print(list)
        print("Sum: ", sum(list))
        print("Średnia: ", (sum(list))/n)