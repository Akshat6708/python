
class programmers:
    company = "Microsoft"
    def __init__(self ,name , salary , email , age):
        self.name = name 
        self.salary = salary
        self.email = email
        self.age = age

A= programmers("akshat " , 500000 , "akshatpatidar@gmail.com" , 22 )
print(A.name , A.email , A.age ,A.salary, A.company)
B= programmers("aman " , 100000 , "amanpatidar123@gmail.com" , 23 )
print(B.name , B.email , B.age ,B.salary , B.company)
C = programmers("ajay " , 500 , "ajaypatidar432@gmail.com" ,20  )
print(C.name , C.email , C.age ,C.salary, C.company)
