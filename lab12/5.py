import re

text=input("numer")
mac=r"^([+48][0-9]{9})"
print(mac)
if re.match(mac, text) is not None:
    print("Ok")
else:
    print("No")
