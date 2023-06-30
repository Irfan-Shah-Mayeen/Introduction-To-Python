from tkinter import *

def display():
    if(x.get()==1):
        print("You agree")
    else:
        print("You don't agree")

window=Tk()
x=IntVar()

python_photo = PhotoImage(file='img.png')
check_button=Checkbutton(window,text="I agee",
                         font=('Arial',20),
                         fg="Green",
                         bg="RED",
                         activeforeground="orange",
                         activebackground="blue",
                         variable=x,
                         onvalue=1,
                         offvalue=0,
                         command=display,
                         padx=25, pady=10,
                         image=python_photo,
                         compound='left')

check_button.pack()
window.mainloop()