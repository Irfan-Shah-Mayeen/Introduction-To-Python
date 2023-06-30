from tkinter import *
#WIDGETS = gui ELEMENT: BUTTON,TEXTBOXES,LABELS,images
#windows = serve as a container to hold or contain these widgets

window = Tk()                #instantiate an instance of  a window
window.geometry("420x420")   # ("width x height "
window.title("Irfan")        #set title

#set icon
icon =PhotoImage(file='logo.png' )
window.iconphoto(True,icon)

#change backround color
window.config(background="skyblue")

#display
window.mainloop()            #place  window on computer screen,listen for event

