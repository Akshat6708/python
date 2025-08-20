from functools import reduce
def greater(a , b):
    if(a>b):
        return a
    return b

l = [10,4,5,3,325,24,1,34,34,5,33,55,4444,24,24]

print(reduce(greater , l))