import time

print(time.ctime(0)) #convert a time expressed in seconds since epoch to a readable string
                     #epoch=when your computer thinks time began(reference point)

print(time.time())  #return current seconds since epoch

print(time.ctime(time.time()))  # current date and time
#or
time_object = time.localtime()
#time_object = time.gmtime()   #utc time
print(time_object)
#time object convert as a readable format
local_time=time.strftime("%B %d %Y %H : %M :%S",time_object)
print(local_time)          # %B = month , %d =date %y =year ,%H =hour, %M=minute %S = second

##
time_string="28 April, 2023"
time_object=time.strptime(time_string,"%d %B, %Y")
print(time_object)

##
time_tuple=(2023,4,20,4,20,10,0,0,0)  #(year,month,day,hour.minute,second,week day (start from monday =0,day of year,daylight saving time(0/-1)
time_string=time.asctime(time_tuple)
print(time_string)


