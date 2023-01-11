list=[]
n=1
while n%10 != 0:
    n=int(input("Podaj liczby: "))
    list.append(n)
print(list)

print("Min: ",min(list))
print("średnią:", sum(list)/(len(list)))