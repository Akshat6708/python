
'''
print this pattern  
********
*******
******
*****
****
***
**
*
'''

def pettern(n):
    if(n==0):
         return
    print("*"*n)
    pettern(n-1) 

n = int(input("Enter the number : "))
pettern(n)