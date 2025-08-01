'''
1 for snake,
-1 for water 
0 for gun
'''
import random

computer = random.choice([-1,0,1])
youstr= input("Please choose one from 's', 'w', or 'g' : ")
youDict = {"s":1 , "g":0 , "w":-1}
reverseDict={1:"snake", -1:"water" , 0:"gun"}

you = youDict[youstr]

print(f"computer choise : {reverseDict[computer]}  ")
print(f"Your choise is : {reverseDict[you]}")

if(computer == you):
    print(" draw ! ")
else:
    if(computer==-1 and you==0):
        print("you Loss ! ")

    elif(computer==-1 and you==1):
        print("you Win ! ")

    elif(computer==1 and you==0):
        print("you Win ! ")

    elif(computer==1 and you==-1):
        print("you Loss ! ")

    elif(computer==0 and you==-1):
        print("you Win ! ")

    elif(computer==0 and you==1):
        print("you Loss ! ")

    else:
        print("something want wrong !")
   
    