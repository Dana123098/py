import re
text=input("Imie (2 Imię) i Nazwisko: ")
mac=r"^([A-Ż]{1}[a-ż]{1,23} [A-Ż]{1}[a-ż]{1,23} [A-Ż]{1}[a-ż]{1,23})$"
#print(mac)
if re.match(mac, text) is not None:
    print("Ok")
else:
    print("No")




