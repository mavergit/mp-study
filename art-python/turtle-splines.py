import tkinter
import time
import math
import random
#from rich import print
import turtle
from turtle import *
turtle.tracer(1,1)
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
t.width(2)
t2=t.clone();t2.shapesize(5)
t3=t.clone();t3.shapesize(5)
t.shapesize(5)
t3.color('green')
t2.color('red')


def spline3p(p1,p2,p3):
    helper=turtle.Turtle();helper.speed(0);helper.width(1)
    t.up();t2.up();t3.up() 
    t.setpos(p1);t.dot()
    t2.setpos(p2);t2.dot()
    t3.setpos(p1);t3.dot()
    t.goto(p1);t2.goto(p2);t3.goto(p1)
    t.down()
    t2.down();t3.down()
    
    N=10**1
    r=100
    omega=10
    p10=p1[0];p11=p1[1]
    p20=p2[0];p21=p2[1]
    for i in range(0,N+1):
        s=i/N
        
        #p1[0]=r*(math.cos(omega*s)-1)+p10
        #p1[1]=r*math.sin(omega*s)+p11
        
        #p2[0]=r*(math.cos(omega*s)-1)+p20
        #p2[1]=r*math.sin(omega*s)+p21      
        #p3[0]+=random.randrange(-10,10)
        v1=[0,0]
        v1[0]=(1-s)*p1[0]+s*p2[0]
        v1[1]=(1-s)*p1[1]+s*p2[1]
        t.goto(v1);t.dot(5)
        v2=[0,0]
        v2[0]=(1-s)*p2[0]+s*p3[0]
        v2[1]=(1-s)*p2[1]+s*p3[1]
        t2.goto(v2);t2.dot(5)
        f=[0,0]
        f[0]=(1-s)*v1[0]+s*v2[0]
        f[1]=(1-s)*v1[1]+s*v2[1]
        helper.speed(0)
        helper.clear();helper.up();helper.goto(t.pos());helper.down()
        helper.speed(3)
        helper.goto(f)
        turtle.delay(200)
        helper.dot(5)
        turtle.delay(0)
        helper.goto(t2.pos())
        t3.setpos(f);t3.dot(5)
        
        

def gotocoor(x, y):
    screen.onscreenclick(None)
    t.up();t.goto(x, y);t.down()
    soto=t.pos()
    print(soto)
    p1=t.pos()
    
    spline3p(p1,p2,p3)

    return soto

p1=[-400,-200]

p2=[0,200]
p3=[400,-200]
spline3p(p1,p2,p3)
#screen.onclick(gotocoor)



turtle.update()
turtle.done()
#turtle.exitonclick()
