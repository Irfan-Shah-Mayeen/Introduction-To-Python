#multiple inheritance = when a childclass is derived from more than one parent class
class Prey:
    def flee(self):
        print("The animal fless")

class Predator:
    def hunt(self):
        print("The animal is hunting")
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):     #multiple inheritance
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()

fish.flee()      #fish can use both Prey and Predator class function's
fish.hunt()