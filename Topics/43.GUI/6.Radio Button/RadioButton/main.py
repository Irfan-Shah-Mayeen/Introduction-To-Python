#radio button = similar to check box, but you can select one from a group

from tkinter import *

food=["Pizza","Burger","Hot_Dog"]

def order():
    if(x.get()==0):
        print("You select Pizza")
    elif(x.get()==1):
        print("You order Burger")
    elif(x.get()==2):
        print("You order Hotdog")
    elif (x.get() == 1):
        print("You order Burger")
    else:
        print("Nothing")


window=Tk()

pizzaImage=PhotoImage(file='pizza.png')
burgerImage =PhotoImage(file='burger.png')
hotdogImage=PhotoImage(file='hotdog.png')
foodImages = [pizzaImage,burgerImage,hotdogImage]

x=IntVar()

for i in range(len(food)):
    radiobutton=Radiobutton(window,
                            text=food[i], #adds text to radio button
                            variable=x,  #groups radiobutton together if they share the samne variable
                            value=i ,   #assigns each radiobutton a differenet value
                            padx=25 , # adds padding on x-axis
                            font=("Impact",20),
                            image=foodImages[i], #adds images radiobutton
                            compound='left', #adds image & text(left-side)
                            indicatoron=0, #eliminate circle indicator
                            command=order)  #set cammand of radiobutton to function

    radiobutton.pack()

window.mainloop()