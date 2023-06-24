#keyword arguments = argument preceded by an indentifier when we pass them to a function
#                   The order of the arguments doesn't matter,unlike positional arguments
#                   python knows the names of the arguments that our function receieves
def hello(first,middle ,last):
       print("Hello "+first+" "+middle+" "+last)
hello("Irfan","shah","Mayeen")
hello("Shah","Irfan","Mayeen")
hello(middle="shah",first="Irfan",last="Mayeen")
