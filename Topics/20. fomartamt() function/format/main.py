#str.format() = optional method that gives users
#               more control when displaying output

animal = "cow"
item = "moon"
print("The "+animal+" jumped over the "+item)

#using format method
animal = "cow"
item = "moon"
print("The {} jumped over the {}".format("cow","moon"))
#or
animal = "cow"
item = "moon"
print("The {} jumped over the {}".format(animal,item))

animal = "cow"
item = "moon"
print("The {0} jumped over the {1}".format(animal,item))
print("The {3} jumped over the {2}".format("tiger","Lion","Moon","Cat"))

#key word argument
print("The {animal} jumped over the {item}".format(animal="lion",item="moon"))

#using string
text = "The {} jupmed over the {}"
print(text.format("Tiger","moon"))
#space
name="Irfan"
print("hello,my name is {}.Nice to meet you".format(name))
print("hello,my name is {:20}. Nice to meet you".format(name))
print("hello,my name is {:<20}. Nice to meet you".format(name)) #right
print("hello,my name is {:>20}. Nice to meet you".format(name)) #left
print("hello,my name is {:^20}. Nice to meet you".format(name))  #central
#format number
number = 3.14159
print("The number pi is {}".format(number))
print("The number pi is {:.2f}".format(number))
print("The number pi is {:.3f}".format(number))

number = 1000
print("The number is {}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number)) #binary
print("The number is {:o}".format(number))#ocatal
print("The number is {:x}".format(number)) #hexa-decimal  lowercase
print("The number is {:X}".format(number)) #hexa-decimal  uppercase
print("The number is {:E}".format(number)) #sciencific notation


