

def Divisibleby5(n):
    if(n%5==0):
        return True
    return False

l = [1,56,57,46,2444,555,35,75,757,10,1780,35,8680,68,56,65,35365,9074]

newList = list(filter(Divisibleby5 , l))

print(newList)