from tkinter import *
#entry widget = textbox that accepts a single line of  user input

window =Tk()
def submit():
    username = entry.get()
    print(username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)
def backspace():
    entry.delete(len(entry.get())-1,END)

entry=Entry(window,
            font=("Arial",50),
            fg="green",
            bg="black",
            show="*")
entry.insert(0,'defaulttext')

entry.pack(side=LEFT)

submit_button = Button(window,text="Submit",command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="Delete",command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text="Back_Space",command=backspace)
backspace_button.pack(side=RIGHT)


window.mainloop()