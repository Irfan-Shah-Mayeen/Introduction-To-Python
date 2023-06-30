#walrus operator :=
#new to python 3.0
#assignment expression aka walrus operator
#assigns values to variables as part of a larger expression

#happy =True
#print(happy)
       #or
#print(happy=True)   # it will error
       #walrus operator

print(happy := True)

#example

#foods = list()

#while True:
#    food  = input("What food do you like : ")
#    if food =="quit":
#        break
#    foods.append(food)

#print(foods)

               #or
foods = list()
while food := input("what food do you like: ")!="quit":
    foods.append(food)

print(foods[0])
