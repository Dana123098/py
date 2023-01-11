# obrać od użytkownika liczbę w zakresie 0 – 999 (w przypadku niespełnionego
# warunku wypisać stosowny komunikat). W programie wyświetlić sumę cyfr oraz
# liczbę: jedności, dziesiątek i setek składających się na podaną liczbę (podpowiedź: w
# zadaniu wykorzystać operator reszty z dzielenia)

a = int(input("Podaj liczbe w zakresie 0 – 999: "))
if a>=0 and a<=999:
    # print("Suma cyfr - {}".format(sum([int(x) for x in str(a)])))
    # print("Jednosci - {}".format(a%10))
    # print("Dziesiatki - {}".format(int(a/10%10)))
    # print("Setki - {}".format(int(a/100%10))) 
    
    b=a//100
    d=a//10%10
    f=a%10 
    print(b)
    print(d)
    print(f)
    sum=b+d+f
    print("Sum",sum)
else:
    print("sprobuj jeszcze")
/