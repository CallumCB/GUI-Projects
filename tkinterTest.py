from tkinter import *
top = Tk()
playList=[]
def results():
    result=E1.get()
    print(result)
    print(type(result))
def addToList():
    newItem = E1.get()
    playList.append(newItem)
L1 = Label(top, text="Hello, world")
L1.grid(column= 0, row= 1)

E1 = Entry(top, bd = 5)
E1.grid(column= 0, row= 2)

B1 = Button(text= "  Get data  ", bg="green", command=results)
B1.grid(column= 0, row= 3)

B2 = Button(text = "Add to List", bg= "red", command =addToList)
B2.grid(column=2, row=2)
top.mainloop()
