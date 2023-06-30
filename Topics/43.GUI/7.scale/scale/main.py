from tkinter import *

def submit():
    print("The temperaure is : "+ str(scale.get())+" degree C")

window=Tk()

hotImage = PhotoImage(file='flame.png',width=200,height=200)
hotLabel=Label(image=hotImage)
hotLabel.pack(side="top")

coldImage=PhotoImage(file='snow.png',width=200,height=200)
coldLabel=Label(image=coldImage)
coldLabel.pack(side="bottom")

scale = Scale(window,from_=1,to=100,
              length=600,
              orient=VERTICAL,
              font=('Consolas',20),
              tickinterval=10,  #adds numeric indicator for value
              #showvalue=0)      #hide current value
              resolution=5,     #increment of slider
              troughcolor="Green",
              fg="Blue",
              bg="black")



#scale.set(50)
#or
scale.set(((scale['from']-scale['to'])/2)+scale['to'])

scale.pack()

button =Button(window,text="submit",command=submit)
button.pack()
window.mainloop()