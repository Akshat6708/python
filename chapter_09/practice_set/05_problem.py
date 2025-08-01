
words = ["Akshat" , "Aman" , "Ajay" , "Hariom" , "Arvind"]

with open("05_problem.txt", "r")as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#"*len(word))

with open("05_problem.txt" , "w") as f : 
    f.write(content)