class calculator:
    def __init__(self , n):
        self.n = n

    def square(self):
        print(f"square of {self.n} is : {self.n*self.n}")

    def cube(self):
        print(f"the cube of {self.n} is : {self.n*self.n*self.n}")
    
    def squareroot(self):
        print(f"The squareRoot of {self.n} is {self.n**1/2}")

    @staticmethod 
    def hello():
     print("hello jee")


a=calculator(4) 
a.hello()
a.square()
a.squareroot()
a.cube()