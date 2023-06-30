from car import Car

car1= Car("Chevy","Corvette",2024,"red")
car2= Car("ford","mustang",2022,"blue")
car3 =Car("motorcycle","yamaha",2022,"black")



print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)

car1.drive()
car1.stop()

print(car2.make)
print(car2.model)
print(car2.year)
print(car2.color)
car2.drive()

print(car1.wheels)
print(car2.wheels)
car3.wheels=2
print(car3.wheels)  #it will change only car3 wheels
car.wheels=2  # it will change for all wheel



