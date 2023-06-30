#prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

#abstract cass = a class which contains one or more abstract method
#abstract method = a method that has a decleration but does not an implementations

from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("you drive the car")
    def stop(self):
        print("This car is stop")

class Motorcycle(Vehicle):
    def go(self):
        print("you ride the motorcycle")
    def stop(self):
        print("This motorcyle is stop")

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()