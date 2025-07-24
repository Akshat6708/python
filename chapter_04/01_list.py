
friend =["banana", "apple ", 23, 23.54, True , "akshat"]
print(friend)
friend[0]="grapes"  # list is mutable that means list ko change kiya ja sakta h per 
# string is immutable that means string ko change kiya ja sakta h 
print(friend)


# some methods of the list 

#slice of list
# print(friend[1:4])

# append -> add at the end of the list 
print(friend.append("hariom"))
print(friend)

# friend.pop()
# print(friend)

# add some list at the end of main list
friend.extend([2,99,"aman"])
print(friend)

# instert 
friend.insert(2,99)
print(friend)

# pop 
friend.pop(3)
print(friend)


# sort 
list1 = [53,4,53,545,24,24,254,6]
list1.sort()
print(list1)


# reverse
list2=[2,54,35,46,24,54,3]
list2.reverse()
print(list2)

# remove 
list2.remove(46)
print(list2)