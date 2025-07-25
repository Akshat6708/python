# find the sum of first natural number 

n = int(input("Enter the number : "))
i = 1 
Totalsum = 0
while(i<=n):
    Totalsum += i
    i +=1
print(f"sum of first {n} natural number is : {Totalsum}")