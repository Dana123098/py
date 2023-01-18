import re
# text=input("imie i nazwisko")
# mac=re.findall(r"^([A-Z][a-zA-Z]{3,11})_([A-Z][a-zA-Z]{3,11})$", text)
# # if mac == True:
# #     print("Ok")
# # elif mac==False:
# #     print("non")    
# print(mac)
# while True:
#     print("ok")

#     break


# if mac== None:
#     print("non")

#1##
# text=input("imie i nazwisko")
# mac=r"^([A-Ż]{1}[a-ż]{1,23} [A-Ż]{1}[a-ż]{1,23})$"
# #print(mac)
# if re.match(mac, text) is not None:
#     print("Проверка пройдена")
# else:
#     print("Провера не пройдена")

##2
# import re
# email = "me@host."

# pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"

# if re.match(pattern, email) is not None:
#     print("Проверка пройдена")
# else:
#     print("Провера не пройдена")


#3## non
 
# import re

# regex = re.compile(r'(\d+)|([\+-]?\d+)')

# s = "1 2 3 4 5 6 +1 +2 +3 -1 -2 -3 +654 -789 321"
# for r in regex.findall(s):
#     if r[0]:
#         # whole (unsigned)
#         print ('liczbą całkowita - ', r[0])
#     elif r[1]:
#         # a signed integer
#         print ('signed', r[1])


#4##

# text=input("adres")
# mac=r"^([A-Ż]{1}[a-ż]{1,50}_[0-9]*)$"
# print(mac)
# if re.match(mac, text) is not None:
#     print("Проверка пройдена")
# else:
#     print("Провера не пройдена")


#5##

# text=input("numer")
# mac=r"^([+48][0-9]{9})"
# print(mac)
# if re.match(mac, text) is not None:
#     print("Проверка пройдена")
# else:
#     print("Провера не пройдена")