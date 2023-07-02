from tkinter import *
from tkinter import filedialog

def saveFile():
    file=filedialog.asksaveasfile(defaultextension='.txt',
                                  filetypes=[
                                      ("Text file",".txt"),
                                      ("HTML file",".html"),
                                      ("All file",".*"),
                                  ])
    file_text=str(text.get(1.0,END))
    file.write(file_text)
    file.close()

window=Tk()

button=Button(window,text="save",command=saveFile)
button.pack()

text=Text(window)
text.pack()

window.mainloop()