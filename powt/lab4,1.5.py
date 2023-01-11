n=int(input("podaj ile liczb(nie<4): "))
list=[]
list2=[]
i=0

while i<n and n>4:
    m=int(input("podaj liczby:"))
    list.append(m)
    i+=1
print(list)

def max_three_sum(arr):
    lst =[] # заводим пустой список
    while len(lst) < 3: # пока в списке меньше 3х чисел
        max_el = arr.pop(arr.index(max(arr))) # извлекаем максимальный элемент по индексу
        if max_el not in lst: # проверяем на наличие в созданном списке
            lst.append(max_el) # добавляем если такого еще нет
    print(sum(lst)) # выводим сумму 3х максимальных элементов

/
max_three_sum(list)

