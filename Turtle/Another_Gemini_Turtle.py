import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("red")

t.penup()

t.goto(-150, -150)

t.pendown()
t.circle(150)
t.setheading(90)
t.forward(100)

turtle.done()