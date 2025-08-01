
with open("08_problem.txt")as f:
    content= f.read()

with open("copy_08_problem.txt", "w") as f:
    f.write(content)
