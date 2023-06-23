#conditiom

age =int(input("Enter your age:"))
if age>=18 :
    print("Your are an adult")
elif age==12:
    print("you are 12 years old")
elif age<0:
    print("You have not born")
else:
    print("you are a child")

 #logical operator
temp=float(input("Enter temperature"))

if not temp >= 0 and temp <= 30:
    print("Weather is good")
    print("Go outside!")
elif not temp<0 or temp>30:
     print("the weather bad today")
     print("Don't Go!")

