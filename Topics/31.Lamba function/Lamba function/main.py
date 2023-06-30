#lambda function = function written in  1 line using lambda keyword
#                 accepts any number of argument , but only has one expression
#                 (think of it as shortcut)
#                 (useful if need for a short period of time , throw-away)
#lambda parameers : expression
def double(x):
    return x * 2

print(double(5))

      #or
double = lambda x:x*2
print(double(5))

        #2 parameter
multiply = lambda x,y : x*y
print(multiply(5,6))
         #3 paramter
add = lambda x,y,z : x+y+z
print(add(5,6,7))

#string

full_name = lambda first_name,last_name : first_name+" "+last_name
print(full_name("Irfan","Shah"))

#age_check = lambda age : True if age >=18 else False
#print(age_check(18))




