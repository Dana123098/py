5.4
n = int(input("Wproadz ile chzcesz liczb:"))
list = []
i = 0
while i < n:
    m = int(input("Wprowadz liczy: "))
    list.append(m)
    i+=1
print(list)
for i in list:
    if i % 2 == 0:
        list.sort(key=lambda i:(i%2, not i%2))
print(list)