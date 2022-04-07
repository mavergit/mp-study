import tkinter
import turtle
import time
import math
import random
turtle.tracer(10,0)

turtle.colormode(255)
t=turtle.Turtle()
t.speed(0)
def drawmany():
    xcors=[];ycors=[];rs=[]
    for i in range(10**4):
        t.width(random.randrange(2,7))
        x=random.randrange(-400,400);xcors.append(x)
        y=random.randrange(-400,400);ycors.append(y)
        t.up();t.goto(x,y);t.down()
        t.color(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        r=random.randrange(10,40);rs.append(r)

        if r<30: 
            t.begin_fill()
            t.circle(r, 360,256)
            t.end_fill()
        elif r>=30:
            t.circle(r, 360,256)

drawmany()
def drawarcs():
    xcors=[];ycors=[];rs=[]
    t2=t.clone()
    t2.up();t2.goto(-400,-200);t2.down()
    for i in range(10**5):
        t.width(random.randrange(2,7))
        t.color(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        r=random.randrange(10,20);rs.append(r)
        t.fd(r);t.lt(random.randrange(-180,180))
        #t.circle(r, random.randrange(-120,120),64)
        
        t2.goto(t2.xcor()+1/2,t.distance(0,0)/10-200)


#drawarcs()
turtle.update()
turtle.exitonclick()