# #1
# import re
# n=int(input("Podaj N="))
# i=0
# list=[]
# while i<n:
#     list.append(i)
#     i+=1
# print(list)

# list2=str(list)

# f=re.findall(r"9", list2)
# print(len(f))

# 2
# a = int(input("Ile chczesz liczb: "))
# list = []
# i=0
# d=0
# while i < a:
#     m = int(input("Wprowadz liczby: "))
#     list.append(m)
#     i+=1
# print(list)

# for i in list:
#     if i == 0:
#         list.sort(key=lambda i:(i==0, not i==0))
# print(list)


#3
n=input("POdaj (): ")
t1=n.count("(")
t2=n.count(")")
if t1==t2:
    print("true")
else:
    print("falsz")