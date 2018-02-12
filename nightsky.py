import turtle

t = turtle.Turtle()


wn=turtle.Screen()
wn.bgcolor("black")
wn.title("A night sky")

def circle(): 

    
    t.up()
    t.goto(-100,200) 
    t.down() 
    t.speed(speed=-300) 
    for x in range(1,360):
        t.forward(1)
        t.right(1)

circle()

turtle.mainloop()