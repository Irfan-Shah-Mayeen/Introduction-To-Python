from tkinter import  *
def openFile():
    print("File opened")
def saveFile():
    print("File saved")
def cut():
    print("You cut text")
def copy():
    print("You copy text")
def paste():
    print("You paste")


window = Tk()

menubar=Menu(window)
window.config(menu=menubar)

fileMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="file",menu=fileMenu)

fileMenu.add_command(label='open',command=openFile)
fileMenu.add_command(label='save',command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=quit)

editMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="cut",command=cut)
editMenu.add_command(label="copy",command=copy)
editMenu.add_command(label="paste",command=paste)

window.mainloop()