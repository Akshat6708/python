import os

file_path = "10_problem.txt" 
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} has been deleted")

else:
    print(f"{file_path} does not exit ")

#remove all content in 10_problem.txt file
# with open("10_problem.txt", "w")as f:
#     f.write("")


#delete a file 
