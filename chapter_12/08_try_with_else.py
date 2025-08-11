
try:
    a= int(input("Enter the number :"))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else block ")

    # jab bhi try block succesfully exicute hoga tabhi else vala case run hoga verna nhi hoga