#function = a block of code which  is executed only when it is called

def hello():
    print("hello!")


hello()
hello()
hello()
def hello1(name):
    print("hello "+name)
    print("Nice to meet you")

hello1("Irfan")

def printName(first_name,last_name):
    print("Hello "+first_name+" "+last_name)

printName("Irfan","Shah")

#return statement = Funtions sed python values/ovjects back to the caller.
                   #these values/object are known as the functions return valu
def multiply(num1,num2):
    result = num1*num2
    return result

x=multiply(5,2)
print(x)
print(multiply(5,3))