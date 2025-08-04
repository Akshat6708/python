
class employee:
    language ="python"
    salary = 100000
    def __init__(self , name , language , salary):
        # in python , dunder method which is automatically called
        self.name = name
        self.language = language
        self.salary= salary
        print("i am a constructor , i am call automatically")
        
    def getinfo(self ):  # self is mandatory
        print(f"employee name is : {self.name}\n employee salary is : {self.salary} \n language is :{self.language}")

   
Akshat = employee("akshat" ,"Java" , 500000)
print(Akshat.name , Akshat.salary , Akshat.language)



