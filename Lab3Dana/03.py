# #1
# import random
# ver = 0
# while (ver == 0):
#     player = int(input("Kamień = 1, Noz = 2, Bum = 3 : "))
#     if (player ==1 or player ==2 or player ==3 ):
#         ver = 1
# if player == 1:
#     print("player : Kamień")
# if player == 2:
#     print("player : Noz")
# if player == 3:
#     print("player : Bum") 
# comp = random.randint(1,3)
# if comp == 1:
#     print(" comp : Kamień")
# if comp == 2:
#     print("comp : Noz")
# if comp == 3:
#     print("comp : Bum") 
# if player == comp:
#     win=0
#     print("0:0")
# if player == 1 and comp == 2:
#     win=1
#     print("Win player")
# if player == 1 and comp == 3:
#     win=2
#     print("Win comp")
# if player == 2 and comp == 1:
#     win=2
#     print("Win comp")
# if player == 2 and comp == 3:
#     win=1
#     print("Win player")
# if player == 3 and comp == 1:
#     win=1
#     print("Win player")
# if player == 3 and comp == 2:
#     win=2
#     print("Win comp")

#2
# import math
# print("Podaj liczbe od 10 do 50")
# n = int(input("n:"))
# b = int(input("b:"))
# a = int(input("a:"))
# if (n and b and a)>10 and (n and b and a)<50:
#     s = n**2+b**2+a**2
#     print(s)
# else:
#     print("No")


#3
print("Podaj liczbe")
a = int(input("a:")) 
if a >255 and a>50000:
    print(a/2)
    
b = int(input("b:"))
if a + b>255 and a*b>50000:
    print((a+b)/2)

d = int(input("d:"))
if a + b + d>255 and a*b*d>50000:
    print((a+b+d)/3)

c = int(input("c:"))
if a + b + d + c>255 and a*b*d*c>50000:
    print((a+b+d+c)/4)

s = int(input("s:"))
if a + b + d + c + s>255 and a*b*d*c*s>50000:
    print((a+b+d+c+s)/5)

n = int(input("n:"))
if a + b + d + c + s + n>255 and a*b*d*c*s*n>50000:
    print((a+b+d+c+s+n)/6)

