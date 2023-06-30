#method chainig = celling multiple methods sequentially
#each cell performs an action on the same object and return self

class Car:
    def turn_on(self):
        print("You start the engine")
        return self
    def drive(self):
        print("you drive the car")
        return self
    def brake(self):
        print("You step on the brake")
        return self
    def tunr_off(self):
        print("You turn off the engine")
        return self

car = Car()
car.turn_on().drive().brake().tunr_off()
car.tunr_off().drive()
car.
