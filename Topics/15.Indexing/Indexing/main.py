#index ioperator []= gives access to a sequences's element (str,list,tuples)

name = "irfan"
if(name[0].islower()):
    name=name.capitalize()
print(name)

name = "irfan Shah"
first_name= name[0:5].upper()
print(first_name)

last_name=name[6:10].lower()
print(last_name)

name = "irfan Shah!"
last_character = name[-1]
second_last =name[-2]
print(last_character)
print(second_last)







