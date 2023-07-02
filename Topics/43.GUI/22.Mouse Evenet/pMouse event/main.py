from tkinter import *

def leftclick(event):
    print("You press left")

def midleclick(event):
        print("You press midlle")
def rightclick(event):
    print("You press right")
def function(event):
    print("Mouse Coordinate "+str(event.x)+","+str(event.y))


window = Tk()


#window.bind("<Button-1>",leftclick)
window.bind("<Button-3>",midleclick)  #moudewheel
window.bind("<Button-3>",rightclick)
window.bind("<Button-1>",function)

window.mainloop()