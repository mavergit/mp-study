import turtle

def up():
    #while ()
    t.setheading(90)
    t.forward(10)
    #t.update()

def down():
    t.setheading(270)
    t.forward(10)
    #t.update()

def left():
    t.setheading(180)
    t.forward(10)
    #t.update()

def right():
    t.setheading(0)
    t.forward(10)
    #t.update()

turtle.onkey(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

t=turtle.Turtle()
#t.fd(100)

turtle.listen()
turtle.update()
turtle.mainloop() 