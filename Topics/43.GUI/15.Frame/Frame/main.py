#frame = a rectangular container to group and hold widgets

from tkinter import  *

window=Tk()

frame=Frame(window,bg='pink',bd=5,relief=RAISED)
#frame.pack(side=TOP)
#or
frame.place(x=0,y=0)

#button = Button(window,text="W",font=("Consolas",25),width=3)
#button.pack(side=TOP)
#shortcut
#Button(window,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
#Button(window,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
#Button(window,text="D",font=("Consolas",25),width=3).pack(side=LEFT)



button = Button(frame,text="W",font=("Consolas",25),width=3)
button.pack(side=TOP)
#shortcut
Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)
window.mainloop()