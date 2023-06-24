#kwargs = parameter that will pack all argument into a dictionary
#          useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
    print("Hello! "+kwargs['first']+" "+kwargs['last'])

hello(first="Irfan",middle="Shah",last="Mayeen" )

def hello(**kwargs):
    print("Hello",end=" ")
    for value in kwargs.items():
        print(value,end=" ")

hello(title="Mr.",first="Irfan",middle="Shah",last="Mayeen")