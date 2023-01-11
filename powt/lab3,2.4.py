wartość = 2
list=[]
while wartość%2==0:
    wart=int(input("Podaj liczbu:"))
    wartość=wart
    list.append(wart)

print(wart)
max=max(list)
min=min(list)
print("Max",max)
print("Min",min)