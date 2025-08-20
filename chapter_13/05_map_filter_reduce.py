from functools import reduce
# map method 
l = [1,2,3,4,5]
squre = lambda x:x*x

squrelist = map(squre, l)

print(list(squrelist))
#   or
# for i in squrelist:
#     print(i)


# filter method

def even(n):
    if(n%2==0):
        return True
    return False

evenlist= filter(even , l)
print(list(evenlist))


# reduce method 
# reduce function ko import kerna padta h funtools se 


def sum(a,b):
    return a+b

def multi(a,b):
    return a*b

print(reduce(sum,l))
print(reduce(multi,l))