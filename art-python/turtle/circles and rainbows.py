import tkinter
import turtle
import time
import math
import random
turtle.colormode(255)
#turtle.tracer(0,0)
t=turtle.Turtle()
t.speed(0)
n=8
step=40
t.up();t.rt(90);t.fd(350);t.lt(90);t.down()
while n>0:
    n-=1
    
    t.begin_fill()
    t.color(random.randrange(n*255//9,255),random.randrange(n*255//9,255),random.randrange(n*255//9,255))
    t.circle(100+step*n)
    t.up();t.lt(90);t.fd(step);t.rt(90);t.down()
    t.circle(100+step*(n-1))
    t.end_fill()
    
turtle.update()
turtle.exitonclick()