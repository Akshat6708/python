

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
    else: 
        return "all numbers are equal"
    

a= int(input("enter the first number: "))
b= int(input("enter the second number: "))
c= int(input("enter the third number: "))

ans = greatest(a,b,c)
print(f"the gratest numner of {a}, {b}, {c} is : {ans}")