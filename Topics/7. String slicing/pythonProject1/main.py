#slicing = create a substring by extracting elements from another string
#indexing[] or slice()
#[star;stop:step]

name ="Irfan Shah"
first_name= name[0:5]
last_name=name[6:10]
print(first_name)
print(last_name)
funky_name=name[0:10:3]
print(funky_name)
funky_name=name[::2]
print(funky_name)
reverse_name= name[::-1]
print(reverse_name)

website = "http://google.com"
website2= "http://facebook.com"
slice = slice(7,-4)
print(website[slice])
print(website2[slice])

