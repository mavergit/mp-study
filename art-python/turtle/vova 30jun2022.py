import turtle
turtle.tracer(0,0)

def draw_many_squares(startx,starty,side,shift,N):
    t=turtle.Turtle()
    t.up()
    t.goto(startx,starty)
    #t.down()
    for k in range(N):
        t.down()
        for i in range(4):
            t.fd(side)
            t.rt(90)
        t.up()
        t.setheading(45)
        t.fd(shift)
        t.lt(90)
        t.fd(shift)
        t.rt(180)

def centered_squares(startx,starty,side,shift,N):
    t=turtle.Turtle()
    t.up()
    t.goto(startx,starty)
    #t.down()
    for k in range(N):
        t.bk(side/2+k*shift)
        t.lt(90)
        t.bk(side/2+k*shift)
        t.rt(90)
        t.down()
        for i in range(4):
            t.fd(side+k*2*shift)
            t.lt(90)
        t.up()
        t.goto(startx,starty)
centered_squares(0,0,100,10,3)
turtle.update()
turtle.done()