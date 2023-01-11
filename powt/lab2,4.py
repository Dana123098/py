import math
a = int(input("Podaj a:"))
b = int(input("Podaj b:"))
c = int(input("Podaj c:"))

if a ==0:
    print("to nie jest równanie kwadratow")
else:
    delta=b**2-4*a*c
if delta==0:
    x0=-b/2*a
    print("X0:",x0)
if delta<0:
    print("brak pierwiastków")
if delta>0:
    x1=(-b-math.sqrt(delta))/2*a
    x2=(-b+math.sqrt(delta))/2*a
    print("X1:",x1,"X2:",x2)
