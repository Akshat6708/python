# readlines function 
#its return a list 

# f = open("file.txt" )
# lines = f.readlines()
# print(lines , type(lines)) 

# readline function 

# f = open("file.txt")
# line1 = f.readline()
# print(line1, type(line1)) 

# line2 = f.readline()
# print(line2) 

# line3 = f.readline()
# print(line3) 

# line4 = f.readline()
# print(line4) 

# line5= f.readline()
# print(line5) 

# line6= f.readline()  # 6th line is not avalable so its return empty string 
# print(line6) 



# readline function loop
f= open("file.txt")
l = f.readline()
while(l != ""):
    print(l)
    l=f.readline()
f.close()