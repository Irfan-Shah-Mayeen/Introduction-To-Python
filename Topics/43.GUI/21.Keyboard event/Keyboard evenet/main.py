from tkinter import *

def doSomething(event):
    print("You did a thing")
def enter(event):
    print("you press enter")
def function(event):
    print("You pressed: "+event.keysym) #show key in console
    label.config(text=event.keysym)



window=Tk()

window.bind("<w>",doSomething)  #press w
window.bind("<Return>",enter)  #press enter
window.bind("<Key>",function)  #press any key

label=Label(window,font=("Helvetica",100))
label.pack()
window.mainloop()