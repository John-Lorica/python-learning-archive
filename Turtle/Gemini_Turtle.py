import turtle

# Soldier 1
t = turtle.Turtle()
t.color("purple")
t.shape("turtle")

# Soldier 2
t2 = turtle.Turtle()
t2.color("orange") # NO equal sign here
t2.shape("arrow")

# Execute Maneuvers
for i in range(4):
    t.forward(100)
    t.right(90)

for i in range(4):
    t2.backward(100)
    t2.left(90)

turtle.done()