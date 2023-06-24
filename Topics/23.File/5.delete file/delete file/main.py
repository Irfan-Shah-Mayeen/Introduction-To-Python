import os
os.remove('test.txt')

#or

path = "test.txt"
try:
    os.remove(path)
    print("File removed")
except FileNotFoundError:
    print("File not found")