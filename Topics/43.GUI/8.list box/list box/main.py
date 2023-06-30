#list box = A listing of selectable text items within it's own container

from tkinter import *
def submit():
    food=[]
    for i in listbox.curselection():
        food.insert(i,listbox.get(i))
    print("You have ordered:")
    for i in food:
        print(i)
   # print(listbox.get(listbox.curselection()))
def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())
def delete():
    for i in listbox.curselection():
        listbox.delete(i)
    #listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg="SKYblue",
                  font=("Constantia",35),
                  width=12,
                  selectmode=MULTIPLE)


listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"Pasta")
listbox.insert(3,"Burger")
listbox.insert(4,"Hot dog")
listbox.insert(5,"Coffe")

listbox.config(height=listbox.size())

entryBox=Entry(window)
entryBox.pack()

submit_buttom=Button(window,text="Submit",command=submit)
submit_buttom.pack()

addButton = Button(window,text="add",command=add)
addButton.pack()

deleteButton =Button(window,text="Delete",command=delete)
deleteButton.pack()
window.mainloop()