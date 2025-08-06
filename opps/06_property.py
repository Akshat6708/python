
class Car:
    def __init__(self , model , brand):
        self.__model = model 
        self.__brand= brand

    def get_brand(self):
        return self.__brand + "!"
    
    def fuleType(self):
        return "diesel or patrol"
    
    @property  # iski vajha se vhalue ko overwrite nhi kiya ja sakta 
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, model , __brand ,batterySize):
        super().__init__(model, __brand)
        self.batterySize = batterySize
    def fuleType(self):
        return "Electric charge"
    @staticmethod
    def detail():
        print("I have a black Thar")
    
my_car= ElectricCar( "S8","tasla" , "85KwH")
c= Car("tata" , "brazza")
# c.model = "swift"
print(c.model)



