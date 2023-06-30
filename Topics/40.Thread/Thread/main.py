#thread = a flow of execution.Like a separate order of instructions.
#         however each thread takes a turn running to achieve concurrency
#         GIL - global interpreter lock
#         allows only one thread to hold the control of the python interpreter

#cpu bound = program/task spends most of it's time waiting for the internal events (cpu intensive) use multiprocessor)

#IO bound = program/task spends most of it's time waiting for external events (user input,web scraping) use multithreading)

import threading
import time

print(threading.active_count())
print(threading.enumerate())

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")
def drink_coffe():
    time.sleep(4)
    print("You drink coffe")
def study():
    time.sleep(5)
    print("you finished study")

x = threading.Thread(target=eat_breakfast,args=())
x.start()

y = threading.Thread(target=drink_coffe,args=())
y.start()

z = threading.Thread(target=study,args=())
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

#eat_breakfast()
#drink_coffe()
#study()