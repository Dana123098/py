#5.5
# n = int(input("Wpisz ile chczesz liczb:"))
# list =[]
# i = 0
# while i < n:
#     m = int(input("Wpisz liczby:"))
#     list.append(m)
#     i+=1
# print(list)
# for i in list:
#     if i % 5 == 0:
#         list.remove(i)
# print(list)

#4
# n = int(input("Wpisz ile chczesz liczb:"))
# list1 = []
# i = 0
# while i < n:
#     m = int(input("wpisz liczby:"))
#     list1.append(m)
#     i+=1
# print(list1)
# for i in list1:
#     if i % 2 == 0:
#         list1.sort(key=lambda i:(i%2, not i%2))
     
# print(list1)


#2
# n = int(input("Wpisz ile chczesz liczb:"))
# list1 = []

# i = 0
# while i < n:
#     m = int(input("wpisz liczby:"))
#     list1.append(m)
#     i+=1
# print(list1)
# for i in list1:
#     if i < list1[len(list1)-1]:
#         list1.remove(i)
#         print(list1)
#         print("Sum: ", (sum(list1)))
#         print("Średnia: ", (sum(list1))/n)


#3
n = int(input("Wpisz ile chczesz liczb:"))
list1 = []
list2 = []
i = 0
while i < n:
    m = int(input("wpisz liczby:"))
    list1.append(m)
    
    i+=1
print(list1)

sum = 0
for m in list1:
    while (m != 0 and m > list1[len(list1)-1]):
        sum = sum + m % 10
        m = m // 10
      
print("Сумма цифр числа равна: ", sum)
print(list1)
for i in list1:
    if sum > list1[-1]:
        list1.remove(i<list1[len(list1)-1])
        print(list1)


