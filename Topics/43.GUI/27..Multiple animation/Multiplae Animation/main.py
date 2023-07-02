from tkinter import *
from Ball import *
import time


window=Tk()

WIDTH=500
HEIGHT=500

canvas=Canvas(window,width=WIDTH,height=HEIGHT,bg="light blue")
canvas.pack()

volley_ball=Ball(canvas,0,0,100,1,1,"orange")
tennis_ball=Ball(canvas,0,0,50,4,1,"green")
pinkponk_ball=Ball(canvas,0,0,25,3,4,"yellow")
foot_ball=Ball(canvas,0,0,120,4,3,"Black")
hockey_ball=Ball(canvas,0,0,70,4,4,"white")
basket_ball=Ball(canvas,0,0,80,5,8,"Red")

while True:
    volley_ball.move()
    tennis_ball.move()
    pinkponk_ball.move()
    foot_ball.move()
    hockey_ball.move()
    basket_ball.move()


    window.update()
    time.sleep(0.01)



window.mainloop()