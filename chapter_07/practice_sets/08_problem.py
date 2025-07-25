'''
print this pettern
*
**
***
****
*****
'''

#   method - 1 
# n = int (input("enter the number : "))
# for i in range(1, n+1):
#     print("*" * i , end = "")
#     print("")

# method - 2
n = int (input("enter the number : "))
for i in range(1, n+1):
    star = "*"* i 
    print(star)