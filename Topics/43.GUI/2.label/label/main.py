from tkinter import  *
#label = an area widget that holds text and/or an image within a window

window = Tk()
photo = PhotoImage(file='img.png')

label =Label(window,text="Hello world",
             font=('Arial',40,'bold'),fg="red",bg="black",
             relief=RAISED,bd=30,padx=30,pady=30,
             image=photo,compound='bottom')
label.pack()
#or
#label.place(x=0,y=0)



window.mainloop()