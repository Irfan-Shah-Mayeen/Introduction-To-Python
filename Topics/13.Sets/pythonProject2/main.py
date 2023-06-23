#set = collection which is unordered , unindexed. no duplicate values

food = {"pizza","burger","kacchi"}

for x in food:
    print(x,end=" ")
print()
subject ={"English","Bangla","computer","Bangla","Bangla"}
for x in subject:
    print(x,end=" ")
print()
food.add("rool")
food.remove("burger")
food.clear()

game = {"cricket","football","hockey"}
team = {"Bangladesh","India","Argentina"}
game.update(team)
for x in game:
    print(x,end=" ")
print()
game = {"cricket","football","hockey"}
team = {"Bangladesh","India","Argentina"}
field = game.union(team)
for x in field:
    print(x,end=" ")
print()
print(field)
print()
animal = {"Tiger","Lion","Hen"}
bird = {"Doel","Hen","Duck"}
print(animal.difference(bird))
print(bird.difference(animal))
print(bird.difference(bird))

animal = {"Tiger","Lion","Hen"}
bird = {"Doel","Hen","Duck"}
print(animal.intersection(bird))
print(animal.intersection(animal))
