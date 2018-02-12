import turtle

t = turtle.Turtle()
sides = 5
distance = 400
for i in range(sides):
    t.forward(distance)
    t.right(2*360/sides)
turtle.mainloop()