
#2
# print("Podaj trzy dodatnie liczbys")
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# if a>b and a>c:
#     print("a:",a)
# elif b>a and b>c:
#     print("b:",b)
# else:
#     print("c:",c)



#3
# a = int(input("Podaj liczbe w zakresie 0 – 999: "))
# if a>=0 and a<=999:
#     print("Suma cyfr - {}".format(sum([int(x) for x in str(a)])))
#     print("Jednosci - {}".format(a%10))
#     print("Dziesiatki - {}".format(int(a/10%10)))
#     print("Setki - {}".format(int(a/100%10)))  
# else:
#     print("sprobuj jeszcze")


#4 ax^2+bx+c=0
from cmath import sqrt
import math


a=int(input("a = "))
b=int(input("b = "))
x=int(input("x = "))
c=int(input("c = "))


if a==0:
    print("to nie jest równanie kwadratowe")
else:
    delta=b**2-4*a*c
if delta<0:
    print("równanie nie ma pierwiastków")
elif delta==0:
    x=-b/(2*a)
    print("x0 = ",x)
else:
    x=(-b-math.sqrt(delta))/(2*a)
    x=(-b+math.sqrt(delta))/(2*a)
    print("xl = ",x,"x2 = ",x)






