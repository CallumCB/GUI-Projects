from tkinter import *
import turtle
import random
top = Tk()
playList=[]
myRolls=[]
rollTimes = 0
dieType = 0

def mainMenu():
    clearWindow()
    LMain=Label(top, text = "Block 5 GUI Projects")
    LMain.grid(column=2, row=1)
    
    B1Main=Button(text="Week 1", bg="pink", command = week1, bd = 6)
    B1Main.grid(column=2, row=2)
    
    B2Main=Button(text="Week 2", bg="pink", command = week2, bd = 6)
    B2Main.grid(column=2, row=3)
        
    B3Main=Button(text="Week 3", bg="pink", command = week3, bd = 6)
    B3Main.grid(column=2, row=4)

def results():
    print(playList)
    
def addToList():
    newItem = E1.get()
    playList.append(newItem)
    E1.delete(0, END)

def exportList():
    with open('test.txt', 'w') as f:
        for item in playList:
            f.write("%s\n" % item)

def clearWindow():
    for widgets in top.winfo_children():
        widgets.destroy()

def happyTurtle():
    pen=turtle.Turtle()
    turtle.clearscreen()
    pen.speed(0)
    pen.pensize(6)
    def eye(col, rad):
        pen.down()
        pen.fillcolor(col)
        pen.begin_fill()
        pen.circle(rad)
        pen.end_fill()
        pen.up()
     
     
    pen.fillcolor('#85b4ff')
    pen.begin_fill()
    pen.circle(100)
    pen.end_fill()
    pen.up()

    pen.goto(-40, 120)
    eye('white', 15)
    pen.goto(-37, 125)
    eye('black', 5)
    pen.goto(40, 120)
    eye('white', 15)
    pen.goto(40, 125)
    eye('black', 5)
    
    pen.goto(-40, 85)
    pen.down()
    pen.right(90)
    pen.circle(40, 180)
    pen.up()

def sadTurtle():
    pen=turtle.Turtle()
    turtle.clearscreen()
    pen.speed(0)
    pen.pensize(6)
    def eye(col, rad):
        pen.down()
        pen.fillcolor(col)
        pen.begin_fill()
        pen.circle(rad)
        pen.end_fill()
        pen.up()
     
     
    pen.fillcolor('green')
    pen.begin_fill()
    pen.circle(100)
    pen.end_fill()
    pen.up()

    pen.goto(-40, 120)
    eye('white', 15)
    pen.goto(-37, 125)
    eye('black', 5)
    pen.goto(40, 120)
    eye('white', 15)
    pen.goto(40, 125)
    eye('black', 5)
    
    pen.goto(-40, 50)
    pen.down()
    pen.right(90)
    pen.circle(40, -180)
    pen.up()
def catTurtle():
    turtle.clearscreen()
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(8)
    t.penup()
    t.goto(0,-108)
    t.pendown()

    # draw head 
    for i in range(36):
        t.forward(30)
        t.left(10)

    # draw eyes
    t.penup()
    t.goto(-80,90)
    t.pendown()

    t.left(90)
    for i in range(45):
        t.forward(2)
        t.right(4)

    t.penup()
    t.goto(50,90)
    t.pendown()

    t.left(-180)
    for i in range(45):
        t.forward(2)
        t.right(4)

    # draw nose 
    t.penup()
    t.goto(0,50)
    t.pendown()

    t.setheading(0)

    for i in range(5): 
        t.forward(25)
        t.right(120)
    starting_nose_x = t.xcor()
    starting_nose_y = t.ycor()

    #draw mouth
    t.left(120)
    t.forward(10)
    for i in range(4):

        t.right(16)
        t.forward(17)

    t.penup()
    t.goto(starting_nose_x, starting_nose_y)
    t.pendown()
    t.setheading(-60)

    t.forward(10)
    for i in range(4):
        t.left(16)
        t.forward(17)

    t.penup()
    t.goto(-19, -.10) 
    t.pendown()
    t.right(100)
    for i in range(10):
        t.forward(12)
        t.left(21)

    t.penup()
    t.goto(114, 212) 
    t.pendown()
    t.forward(100)
    t.left(120)
    t.forward(75)

    t.penup()
    t.goto(-107, 193)
    t.pendown()
    t.setheading(75)
    t.forward(100)
    t.right(120)
    t.forward(75)
    t.ht()
def clearTurtle():
    turtle.clearscreen()
def week1():
    clearWindow()
    
    L1 = Label(top, text="Playlist Maker", bg = 'pink')
    L1.grid(column= 0, row= 1)

    E1 = Entry(top, bd = 5)
    E1.grid(column= 0, row= 2)

    B1 = Button(text= " Return List ", bg="green", command= results, bd = 6)
    B1.grid(column= 0, row= 3)

    B2 = Button(text = " + ", bg= "pink", command = addToList)
    B2.grid(column=1, row=2)

    B3 = Button(text= "Export List", bg= "red", command = exportList)
    B3.grid(column=0, row=4)
    
    Bclear=Button(text = "Main menu", bg= 'yellow', command=mainMenu)
    Bclear.grid(column=1, row=3)
    
def week2():
    def rollDice():
        dieType = E1W2.get()
        rollTimes = E2W2.get()

        clearWindow()

        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1,int(dieType)))
       
        L4W2 = Label(top, text = "Here are your rolls!", bg = "LightGoldenrod2")
        L4W2.grid(column = 0, row = 1)
        
        L5W2 = Label(top, text = "{}".format(myRolls), bg = "#a3ff6e")
        L5W2.grid(column = 0, row = 2)
        
        B2W2 = Button(top, text = "Main Menu", bg = "yellow", command = mainMenu, bd = 6)
        B2W2.grid(column = 0, row = 3)
        
    clearWindow()

    L1W2 = Label(top, text = "Dice Roller Program", bg = "gold")
    L1W2.grid(column = 1, row = 1)

    L2W2 = Label(top, text = "How many sides should the die have?", bg = "white")
    L2W2.grid(column = 0, row = 2)

    L3W2 = Label(top, text = "How many times would you like to roll?", bg = "white")
    L3W2.grid(column = 2, row = 2)

    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column = 0, row = 3)

    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column = 2, row = 3)

    B1W2 = Button(text = "Roll!", bg = "pink", command = rollDice, bd = 8)
    B1W2.grid(column = 1, row = 4)

def week3():
    clearWindow()
    pen=turtle.Turtle()
    L1W3 = Label(top, text = "What face do you want?")
    L1W3.grid(column = 1, row = 1)
    
    B1W3 = Button(text = "Happy", bg = 'green', command = happyTurtle)
    B1W3.grid(column = 1, row=2)

    B2W3 = Button(text = "Sad", bg = 'red', command = sadTurtle)
    B2W3.grid(column = 1, row=3)

    B3W3 = Button(text = "Main menu", bg = 'yellow', command = mainMenu)
    B3W3.grid(column = 1, row = 6)

    B4W3 = Button(text = "Cat", bg = 'pink', command = catTurtle)
    B4W3.grid(column = 1, row = 4)

    B5W3 = Button(text = "Clear", bg = 'white', command = clearTurtle)
    B5W3.grid(column = 1, row = 5)
if __name__ == "__main__":
    mainMenu()
    top.mainloop()
