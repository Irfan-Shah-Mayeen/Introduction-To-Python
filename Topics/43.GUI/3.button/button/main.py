from tkinter import  *

#button = you click it , the it does stuff
count=0
def click():
    global count
    count+=1
    print(count)
window = Tk()
photo = PhotoImage(file='cplus.png')

button = Button(window,
                text="Click me",  #button name
                command=click,    #function call(action)
                font=("Comic Sans",30),  #font
                fg="red",
                bg="green",
                activeforeground="blue",  #after click
                activebackground="black", #afte click
                state =ACTIVE,    #if state =DISABLEd ,button will not work
                image=photo,   #umage add
                compound='bottom')

button.pack()
window.mainloop()