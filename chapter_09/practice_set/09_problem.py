
# check both text files are identical or not 

with open("08_problem.txt") as f :
    content1= f.read()

with open("copy_08_problem.txt") as f :
    content2= f.read()

if(content1==content2):
    print("yes, this files are identical")
else:
    print("No, this files are not identical")