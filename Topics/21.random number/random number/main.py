import random
x = random.randint(1,6)   #integer number
print(x)
y = random.random()  #floating number
print(y)

#random choice
myList =['rock','paper','scissors']
z= random.choice(myList)
print(z)

#random suffle
cards=[1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)



