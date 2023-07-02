from tkinter import *
from tkinter import colorchooser #submodule
def click():
   color= colorchooser.askcolor()
   print(color)
   colorRgb=color[0]
   colorHex=color[1]
   print(colorRgb)
   print(colorHex)

   window.config(bg=colorHex)  #change backround color


window =Tk()
window.geometry("420x420")

button=Button(text="Click me",command=click)
button.pack()

window.mainloop()