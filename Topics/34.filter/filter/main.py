#filter() = create a collection of elements from an iterable for which a function return true
#
#filter(function,iterable)

friends = [("Irfan",22),
           ("Nirjon",19),
           ("Ross",17),
           ("joy",15),
           ("Rachel",14)]
age = lambda data : data[1]>=18
drinking_buddies=list(filter(age,friends))

for i in drinking_buddies:
    print(i)