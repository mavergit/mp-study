import tkinter
import time
import math
import random
#from rich import print
import turtle
from turtle import *
turtle.tracer(10,1)
screen=turtle.Screen()
t=turtle.Turtle()

#t.ht()
sizex=1280
sizey=720
step=4
side=2*step/math.sqrt(3)
ww=turtle.window_width();wh=turtle.window_height()
turtle.setup(width=sizex,height=sizey,startx=0,starty=0)
t.color('blue')
t.width(10)
t2=t.clone()
t1=t.clone()
t1.color('green');t2.color('red')


def spline3p(p1,p2,p3):
    t.up();t2.up();t1.up() 
    t.setpos(p1);t.dot()
    t2.setpos(p2);t2.dot()
    t1.setpos(p3);t1.dot()
    t.goto(p1);t2.goto(p2);t1.goto(p1)
    t.down();t2.down();t1.down()
    N=10**3
    for i in range(0,N+1):
        s=i/N
        #print(p1[0])
        v1=[0,0]
        v1[0]=(1-s)*p1[0]+s*p2[0]
        v1[1]=(1-s)*p1[1]+s*p2[1]
        t1.goto(v1)
        v2=[0,0]
        v2[0]=(1-s)*p2[0]+s*p3[0]
        v2[1]=(1-s)*p2[1]+s*p3[1]
        t2.goto(v2)
        f=[0,0]
        f[0]=(1-s)*v1[0]+s*v2[0]
        f[1]=(1-s)*v1[1]+s*v2[1]
        t.setpos(f)

#def recordp():
    point=t.pos()
    return point

#p1=t.onclick(recordp)

def gotocoor(x, y):
    goto = t.goto(x, y)
    print(t.pos())
    return goto

p1=-400,-200
screen.onscreenclick(gotocoor)
#t.dot()
#p1=0,0
p2=0,200
p3=400,-200
spline3p(p1,p2,p3)



turtle.update()
turtle.done()
#turtle.exitonclick()
