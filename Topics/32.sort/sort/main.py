# sort() method = used with lists
#sort() function = used with iterables


#for list
students = ["Irfan","nirjon","alamin","durjoy","touhed"]
print("------Before Sort-------")
for i in students:
    print(i)


students.sort()
print("------After Sort----------")
for i in students:
    print(i)


students.sort(reverse=True)
print("------reverse Sort----------")
for i in students:
    print(i)

#for touple
students = ("Irfan","nirjon","alamin","durjoy","touhed")
sorted_students = sorted(students)  #create a sorted list from touple
print("---------from touple to list-----")
for i in sorted_students:
    print(i)

sorted_students = sorted(students,reverse=True)  # create a sorted list from touple
print("---------Reverse from touple to list-----")
for i in sorted_students:
        print(i)

#level 2
students =[("Irfan","A",25),
           ("Nirjon","D",23),
           ("Alamin","C",31),
           ("Durjoy","B",19),
           ("Touhed","F",22)]
#sort alphabatically
students.sort()
print("--------sort alphabatically-------")
for i in students:
    print(i)

#sort by grade

grade = lambda grades : grades[1]
students.sort(key=grade)
print("-------sort by grade-------")
for i in students:
    print(i)

#rerverse
grade = lambda grades : grades[1]
students.sort(key=grade,reverse=True)
print("-------Reverse sort by grade-------")
for i in students:
    print(i)

#sort by age
age = lambda ages : ages[2]
students.sort(key=age)
print("------sort bye age------")
for i in students:
    print(i)


#touple of touple
students =(("Irfan","A",25),
           ("Nirjon","D",23),
           ("Alamin","C",31),
           ("Durjoy","B",19),
           ("Touhed","F",22))

age = lambda ages : ages[2]
sorted_student = sorted(students,key=age)
print("-----touple of touple sort-----")
for i in sorted_student:
    print(i)