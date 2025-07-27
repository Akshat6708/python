
# convert celsius to fahrenheit
'''
formul for convert 
celsius to fahrenheit = C/5 = f-32/9

'''

def f_to_c(f):
    return 5*(f-32)/9

     


f = int(input("Enter the tempture in F : "))
c= f_to_c(f)
print(f"{round(c,2) }℃")

