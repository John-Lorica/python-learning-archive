import turtle

t = turtle.Turtle()
t.color("purple")
t.shape("turtle")
t2 = turtle.Turtle()
t2.color("orange")
t2.shape("turtle")

for i in range(4):
    t.forward(100)
    t.right(90)
for i in range(4):
    t2.backward(100)
    t2.left(90)

turtle.done()