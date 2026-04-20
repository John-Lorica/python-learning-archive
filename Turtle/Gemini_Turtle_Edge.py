import turtle

#1. Setup
t = turtle.Turtle()
t.shape('turtle')
t.color('red')
wn = turtle.Screen()

#2. Dynamic Limit adjusts your current window size
def get_limit():
    return wn.window_width() / 2 - 30

#3. The safety function
def move_safely(distance):
    limit = get_limit()
    t.forward(distance)
    # if it goes past the limit, move back and turn
    if abs(t.xcor()) > limit or abs(t.ycor()) > limit:
        t.backward(distance + 5)
        t.right(150)

#4 Main Loop
while True:
    # Now you can put any sequence here, and it won't escape!
    move_safely(10)
    t.right(10)
    move_safely(20)
    for i in range(5):
        move_safely(20)
        t.right(72)

    # Even if you add more moves, just use move_safely()
    move_safely(50)