
# tupel is a same as list but it is a mutable that means tuble ko change nhi kiya ja sakta h 

tuple1=(1,4,"akshat ", True)
print(tuple1)

a=(1,2,3,5,6)
print(type(a))   # type -> tuple

b = (1)
print(type(b))   # type -> int
# but we can solve this problem 

c = (2,)
print(type(c))



# some methos of tuples 

# 1. count 

T = (1,2,2,5,2,5,4,64,6,2)
print(T.count(2))  # return occurence of 2

# 2. index 
print(T.index(5)) # its return first index of element 

# Sum of elements

t = (1, 2, 3)
print(sum(t))  # Output: 6


# concadination 
a = (1, 2)
b = (3, 4)
print(a + b)  # Output: (1, 2, 3, 4)

# max ,  min 

maxi = max(T)
mini = min(T)
print(maxi)
print(mini)