
class employee:
    language ="python"
    salary = 100000
    def getinfo(self ):  # self is mandatory
        print(f"employee salary is {self.salary} and language is {self.language}")

    @staticmethod  #this is a static method its not taken a self attribute 
    def greet():
        print("Good morning")

Akshat = employee()
# Akshat.language= "JavaScript"
Akshat.getinfo()
Akshat.greet()
