import os
source ="text.txt"
destination="C:\\Users\\Admin\\Desktop\\text.txt"
try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")

except FileNotFoundError:
    print(source+" "+"was not found")