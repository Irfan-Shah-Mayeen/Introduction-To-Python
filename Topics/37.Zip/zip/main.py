#zip(*iterables) = aggregate elements from two or more iterables(list,tuple,sets,etc)
#                  creates a zip object with paried elements stored in tuple for each element

usernames = ["Irfan","Shah","Mayeen"]
passwords =("p@assword","abc123","guest")

users = zip(usernames,passwords)
for i in users:
    print(i)
print(type(users))

users = list(zip(usernames,passwords))
for i in users:
    print(i)
print(type(users))

users = dict(zip(usernames,passwords))
for key,value in users.items():
    print(key+" : "+value)
print(type(users))

usernames = ["Irfan","Shah","Mayeen"]
passwords =("p@assword","abc123","guest")
login_date =["1/1/2023" , "1/3/2023" ,"2/4/2023"]
users=zip(usernames,passwords,login_date)
for i in users:
    print(i)