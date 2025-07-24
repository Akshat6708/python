
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))
num4 = int(input("Enter the forth number : "))

if(num1 > num2 and num1 > num3 and num1 > num4 ):
    print("Gratest number is ",num1 )
elif(num2 > num1 and num2 > num3 and num2 > num4 ):
    print("Gratest number is ",num2 )
elif(num3 > num1 and num3 > num2 and num3 > num4 ):
    print("Gratest number is ",num3 )
else:
    print("Gratest number is ", num4)
    