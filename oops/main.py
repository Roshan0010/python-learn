class Car:
    cnt=0
    def __init__(self, brand, modal):
        self.__brand = brand
        self.__modal = modal
        Car.cnt+=1
    def getBrand(self):
        return self.__brand
    @property
    def modal(self):
        return self.__modal
    def fuelType(self):
        return "flex-petrol"
    @staticmethod
    def generalDis():
        return "The is a machine which helps us to traverse between distance"

class Battery():
    pass

class Engine():
    pass
    
class Evs(Car,Battery,Engine):
    def __init__(self, brand, modal, battery_capacity):
        super().__init__(brand, modal)
        self.__battery_capacity = battery_capacity
    def getBatteryCapacity(self):
        return self.__battery_capacity
    def fuelType(self):
        return "pure electric charge"

car1=Car("Tata","Nano")
car2=Car("Maruti Suzuki","Wagonar")
ev1=Evs("Tesla","Model S","100kws")

print(car1.getBrand(),car1.modal)
# print(car2.__brand,car2.__modal)
print(ev1.getBrand(),ev1.getBatteryCapacity())
print(ev1.fuelType())
print(car1.fuelType())
# print(car1.cnt)
print(Car.cnt)
print(Car.generalDis())
print(car1.modal)

# print(isinstance(car1,Car))
















