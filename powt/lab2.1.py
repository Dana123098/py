#1 sposud
# print("Gra: Papier, nożyce, kamień")
# print("0–papier, 1–nożyce, 2–kamień")
# user=int(input(("User1:")))
# user2=int(input(("User2:")))

# if user==0 and user2==1:
#     print("Win user2")
# if user==0 and user2==2:
#     print("Win user1")
# if user==0 and user2==0:
#     print("No winer")
# if user==1 and user2==1:
#     print("No winer")
# if user==1 and user2==0:
#     print("Win user1")
# if user==1 and user2==2:
#     print("Win user2")
# if user==2 and user2==1:
#     print("Win user1")
# if user==2 and user2==2:
#     print("No winer")
# if user==2 and user2==0:
#     print("Win user2")


#2 sposub
import random
print("Gra: Papier, nożyce, kamień")
print("0–papier, 1–nożyce, 2–kamień")
user=int(input(("User1:")))
possible_actions=[0,1,2]
computer= random.choice(possible_actions)


if user==0 and computer==1:
    print("Win user2")
if user==0 and computer==2:
    print("Win user1")
if user==0 and computer==0:
    print("No winer")
if user==1 and computer==1:
    print("No winer")
if user==1 and computer==0:
    print("Win user1")
if user==1 and computer==2:
    print("Win user2")
if user==2 and computer==1:
    print("Win user1")
if user==2 and computer==2:
    print("No winer")
if user==2 and computer==0:
    print("Win user2")

