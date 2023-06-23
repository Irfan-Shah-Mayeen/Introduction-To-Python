# list = used to store multiple items in a asingle variable

food = ["pizza" , "burger" , "chicken" ,"hotdog"]
print(food[0])
print(food[1])
print(food[2])

food[0]="roll"
print(food[0])

food.append("ice cream")
food.pop()
food.insert(0,"cake")
food.sort()
#food.clear()
for x in food:
 print(x)