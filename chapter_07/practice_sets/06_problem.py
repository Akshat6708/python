# find the factorial of given number 

n = int(input("enter the number : "))
product =1
for i in range(1, n+1):
    product *=i
    
print(f"factorial of {n} is {product}")