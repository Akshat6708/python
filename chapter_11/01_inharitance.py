
class car :
    color= "Rad"
    company = "maruti suzuki"
    def detail(self):
       print(f"color must be {self.color} and company is {self.color}")
    
   
    
class swift(car):
    carName= "swift"
    modelNo= 72323
    engin="1000 CC"
    def spacificDetail(self):
        
        print(f"car name is {self.carName} color is {self.color} model no : {self.modelNo} company is {self.company} and the engin is {self.engin}")
     


s= swift()
s.spacificDetail()
   