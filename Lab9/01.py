
n = int(input("Wywoływać liczby do liczby "))
i=0
list1=[]
while i<n:
    list1.append(n)
    list1[i]=i
    i+=1  #od 0 do n
 
#zamienić 1=0 bo nie jest liczbo pierwszą
list1[1] = 0
 
m = 1  
while m < n:  # iteracja wszystkich liczb az do podanego
    if list1[m] != 0: 
        j = m * 2  # zwiększamy w 2 razy liczbu
        while j < n:
            list1[j] = 0  # zmeniamy na 0
            j = j + m  # zwiększamy na m
    m += 1

list2 = []
for i in list1:
    if list1[i] != 0:
        list2.append(list1[i])
print(list2)

