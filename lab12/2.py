import re
email = input("podaj emle:")

pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"

if re.match(pattern, email) is not None:
    print("Ok")
else:
    print("NO")


