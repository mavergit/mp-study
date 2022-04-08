import tkinter
import turtle
import time
import math
import random
sizex=1280
sizey=720
ww=turtle.window_width();wh=turtle.window_height()
turtle.setup(width=sizex,height=sizey,startx=0,starty=0)
turtle.tracer(0,0)


t=turtle.Turtle()
t.speed(0)
t.ht()
t.setpos(-540,0)
def drawcircle(t,radius):
    #t.up();
    t.fd(radius);t.lt(90);t.down()
    t.circle(radius)
    #t.up();
    t.rt(90);t.bk(radius);t.down()
radius=100
steps=1800
shift=1
angle=shift/(radius*2*math.pi)*360
for i in range(0,steps):
    drawcircle(t,radius)
    t.lt(angle*i)
    t.up();t.fd(shift);t.down()
    t.rt(angle*(i+1))
    turtle.delay(1000)
    turtle.update()
    t.clear()

turtle.update()
turtle.exitonclick()