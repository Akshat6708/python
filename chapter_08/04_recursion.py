

def factorial(n):
    # base case 
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1) 

num = int(input("Enter the number: "))
print(f"The factorial of {num} is : {factorial(num)}")