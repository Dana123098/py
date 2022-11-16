n = int(input("Wproadz ile chzcesz liczb:"))
list1 = []

i = 0
while i < n:
    m = int(input("Wprowadz liczy: "))
    list1.append(m)
    i+=1
print(list1)
dli = len(list1)
print("Dlina: ", dli)

print("Sum: ",sum(list1))
print("sr", (sum(list1))/n)