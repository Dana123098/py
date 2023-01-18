import re

regex = re.compile(r'(\d+)|([\+-]?\d+)')
s=input("Podaj liczby: ")

for r in regex.findall(s):
    if r[0]:
       
        print ("liczbą całkowita:", r[0])
    elif r[1]:
        print("Wymierne:", r[1])




