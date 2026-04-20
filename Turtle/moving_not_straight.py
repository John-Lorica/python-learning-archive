import turtle

t = turtle.Turtle()
t.color('yellow')
t.shape('turtle')

#Set up screen
wn = turtle.Screen()
#Get screen boundaries (usually center is 0,0)
#width/2 is the right edge, -width/2 is the left
limit = wn.window_width() / 2 - 20

while True:
    t.forward(2)
    #Check if x or y position is past the limit
    if abs(t.xcor()) > limit or abs (t.ycor()) > limit:
        t.right(180)# Turn around!

   
    t.right(50)
    t.left(50)
    t.setheading(-200)

    if abs(t.xcor()) > limit or abs(t.ycor()) > limit:
        t.right(100)
        t.forward(5)#Move it back into the safe zone

    #turtle.done()