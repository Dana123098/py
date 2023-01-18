import re

text=input("adres: ")
mac=r"^([A-Ż]{1}[a-ż]{1,50}_[0-9]{1,50}_[0-9]*)$"
print(mac)
if re.match(mac, text) is not None:
    print("Ok")
else:
    print("No")



