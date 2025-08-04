from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo= trainNo
    def Book(self , fro , to):
        print(f"Ticket is booked in train no {self.trainNo} form {fro} to {to}")
       
    def getStatus(self):
        
        print(f"Train no : {self.trainNo} is running on time")

    def getFare(self , fro , to):
         print(f"Ticket Fare in train no {self.trainNo} form {fro} to {to} is : {randint(300, 1000)}")


t = Train(221026)
t.Book("bhawani mandi " , "Bhopal")
t.getStatus()
t.getFare("bhawani mandi " , "Bhopal")