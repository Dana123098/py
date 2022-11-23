a = int(input("Ile chczesz liczb: "))
list = []
i=0
while i < a:
    m = int(input("Wprowadz liczby: "))
    list.append(m)
    i+=1
print(list)
def znajdzmin(list):
    for r in range(2):
        t=list.pop(list.index(min(list)))
        print("min:", t)
    

znajdzmin(list)

def usun_elementy(list):
    for u in range(2):
        list.pop(list.index(min(list)))
        
usun_elementy(list)
print(list)




    
