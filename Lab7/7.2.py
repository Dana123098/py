a = int(input("Ile chczesz liczb: "))
list = []
i=0
while i < a:
    m = int(input("Wprowadz liczby: "))
    list.append(m)
    i+=1
print(list)
def fun():
    suma=sum(list)
    print("suma: ", suma)
    p=int(input("Podaj elelement \n"))
    list.append(p)
    print(list)
    d=list.pop(-1)

    print(list)
    print(d,"wydal.5 elem.")
fun()