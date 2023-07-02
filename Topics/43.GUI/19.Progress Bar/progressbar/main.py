from tkinter import *
from tkinter .ttk import *
import time
def start():
    tasks=10
    x=0
    while(x<tasks):
        time.sleep(0.09)
        bar['value']+=10
        x+=1
        percent.set(str((x/tasks)*100)+"%")
        text.set(str(x)+"/"+str(tasks)+"tasks completed")
        window.update_idletasks()

window=Tk()

percent=StringVar()
text=StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

parcentLabel=Label(window,textvariable=percent).pack()
tasklabel=Label(window,textvariable=text).pack()

button=Button(window,text="Download",command=start).pack()

window.mainloop()