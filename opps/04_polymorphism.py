
class Car:
    def __init__(self , model , brand):
        self.model = model 
        self.__brand= brand

    def get_brand(self):
        return self.__brand + "!"
    
    def fuleType(self):
        return "diesel or patrol"
    

class ElectricCar(Car):
    def __init__(self, model , __brand ,batterySize):
        super().__init__(model, __brand)
        self.batterySize = batterySize
    def fuleType(self):
        return "Electric charge"
    
my_car= ElectricCar( "S8","tasla" , "85KwH")
print(my_car.fuleType())

safari = Car("safari" , "Tata")
print(safari.fuleType())


