
hindi = int(input("enter the marks of hindi : "))
english = int(input("enter the marks of english : "))
maths = int(input("enter the marks of hindi : "))

avg =( hindi+english+maths)/3

if((hindi >= 33 and english >= 33 and maths >= 33) and avg >=40):
    print("Congratulation you pass all subject ")
    print("you have archive ", avg,"%")

else: 
    print("fail")