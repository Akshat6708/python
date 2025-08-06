
class Car:
    def __init__(self , model , brand):
        self.model = model 
        self.brand= brand
class ElectricCar(Car):
    def __init__(self, model , brand ,batterySize):
        super().__init__(model, brand)
        self.batterySize = batterySize
    
    

my_car= ElectricCar("tasla" , "S8", "85KwH")
print(f"car modale is {my_car.model} and brand is {my_car.brand} and the battery capacity {my_car.batterySize}")
