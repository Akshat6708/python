
# find the sum og first n natural number using recursion 
def Sum_Natural_no(i , n):
    if(i>n):
        return 0
    return i+Sum_Natural_no(i+1 , n)


n = int(input("Enter the number : "))
ans= Sum_Natural_no(1, n)
print(ans)
