import turtle

t = turtle.Turtle()

def circle(): 
    t.pen(fillcolor = "blue", pensize = 5)
    t.up()
    t.goto(-100,200) 
    t.down() 
    t.speed(speed=-300) 
    for x in range(1,360):
        t.forward(1)
        t.right(1)
    


def square():
    t.pen(fillcolor = "purple", pensize = 7)
    t.up()
    t.goto(100,100)
    t.down()
    for n in range(4):
        t.forward(100)
        t.left(90)
       

def octagon():
    t.pen(fillcolor = "yellow", pensize = 4)
    t.up()
    t.goto(-250,250)
    t.down
    for b in range(8):
        t.forward(50)
        t.left(45)

def hexagon():
    t.pen(fillcolor = "azure3")
    t.up
    t.goto(-300,125)
    for l in range(6):
        t.forward(100)
        t.left(30)



square()
circle()
octagon()
hexagon()




turtle.mainloop()