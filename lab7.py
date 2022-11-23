
# def uraw(x):
#     print("Urav:", x, "=", x**2)
# uraw(3)
# for i in range(1,4):
#     uraw(i)
#####################
# def multi(a,b):
#     print(a*b)
# multi(3,4)
################

#cotnye i nie cotnyje
# def cotNiecot(a):
#     if a%2==0:
#         print(a,"cot")
#     else:
#         print(a,"nie cot")
# for i in range(1,20):
#     cotNiecot(i)
######################
#faktorial
# def faktoril(n):
#     pr=1
#     for i in range(2,n+1):
#         pr=pr*i
#     print(pr)
# faktoril(4)
####################
# import turtle
# def move(a):
#     turtle.forward(a)
#     turtle.left(90)
# def drawSquare(a):
#     for i in range(4):
#         move(a)

# def drawSquareColor(a, color):
#     turtle.color(color)
#     turtle.begin_fill()
#     for i in range(4):
#         move(a)
#     turtle.end_fill()

# turtle.speed(1)
# drawSquareColor(60, "red")
# turtle.goto(150,150)

# drawSquareColor(120, "blue")
#################################
#7.1
# a = int(input("Napisz ile masz egzaminów: "))
# list = []
# i=0
# while i<a:
#     m = int(input("Wpisz oceny:"))
#     list.append(m)
#     i+=1
# print(list)
# for i in list:
#     if i>2:
#         print("Zaliczony")
#     else:
#         print("Nie zaliczony")
# s=(sum(list))/a
# def oblicz_srednia():
#     print((sum(list))/a)
    
# oblicz_srednia()

# for i in list:
#     if i > s:
#         list.sort(key=lambda i:(i>s, not i>s))
# print(list)
##################
#7.2










#7.3
# a = int(input("Napisz ile chcesz liczb: "))
# list = []
# i=0
# while i<a:
#     m = int(input("Wpisz liczby od 1 do 100:"))
#     list.append(m)
#     i+=1
# print(list)
# def remove_element(list):

#     for _ in range(2):
#         list.pop(list.index(min(list)))

# remove_element(list)
# print(list)





