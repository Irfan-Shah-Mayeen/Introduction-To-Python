#canvas = widget that is used to draw graph , plots,image in a eindow

from tkinter import *

window=Tk()

canvas=Canvas(window,width=500,height=500)
canvas.create_line(0,0,500,500,fill="RED",width=10)
canvas.create_line(0,500,500,0,fill="Blue",width=10)
canvas.create_rectangle(50,50,250,250,fill="purple",width=10)
#canvas.create_polygon(250,0,500,500,0,500,fill="yellow",outline="black",width=5)
#or
points=[250,0,500,500,0,500]
canvas.create_polygon(points,fill="yellow",outline="black",width=10)

canvas.create_arc(0,0,500,500,style=CHORD,fill="orange",width=10)

canvas.pack()



window.mainloop()