
n = int(input("Enter a number: "))
Table = [n*i for i in range(1,11)]
with open("table.txt", "a") as f:
  f.write(f"Table of {n} is : {str(Table)} \n ")  
  