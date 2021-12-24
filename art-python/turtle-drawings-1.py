import tkinter
import time
import math
import random
#from rich import print
import turtle
from turtle import *
#turtle.tracer(10,0)
t=turtle.Turtle()
t.ht()
sizex=1280
sizey=720
step=4
side=2*step/math.sqrt(3)
ww=turtle.window_width();wh=turtle.window_height()
turtle.setup(width=sizex,height=sizey,startx=0,starty=0)


def drawcircle2():
    t=turtle.Turtle()
    turtle.tracer(60,0)
    #t.ht()
    t.speed(0)
    #t.setpos(0.0,0.0)
    #print(t.pos())
    for i in range(360):
        t.forward(1)
        t.left(1)
        
#drawcircle2()

def drawxlines(step):
    t=turtle.Turtle()
    turtle.tracer(0,0)
    t.speed(0)
    t.ht()
    t.up()
    t.setpos(-sizex/2+step,-sizey/2+step)
    t.down()
    for i in range(int(sizey/step)):
        t.fd(sizex-2*step)
        t.up()
        t.setpos(-sizex/2+step,-sizey/2+step+step*i)
        t.down()

def drawylines(step,angle):
    t=turtle.Turtle()
    turtle.tracer(0,0)
    t.speed(0)
    t.ht()
    t.up()
    t.setpos(-sizex/2+step-(sizey-2*step)/math.sqrt(3),sizey/2-step)
    t.right(angle)
    t.down()
    for i in range(int((sizex+(sizey-2*step)/math.sqrt(3))/step)):
        t.fd((sizey-2*step)*2/math.sqrt(3))
        t.up()
        t.setpos(-sizex/2+step-(sizey-2*step)/math.sqrt(3)+step*i*2/math.sqrt(3),sizey/2-step)
        t.down()    
#drawxlines(step)
#drawylines(step,60)
#drawylines(step,120)

def drawxlinesfor6(step):
    t=turtle.Turtle()
    turtle.tracer(0,0)
    t.speed(0)
    t.ht()
    t.up()
    t.setpos(-sizex/2+step,-sizey/2+step)
    t.down()
    for i in range(int(sizey/(2*step))):
        for j in range(int((sizex-2*step)/(3*side))+1):
            t.fd(side)
            t.up()
            t.fd(2*side)
            t.down()
        t.up()
        t.setpos(-sizex/2+step+side*1.5,-sizey/2+step+step*(2*i+1))
        t.down()
        for j in range(int((sizex-2*step-1.5*side)/(3*side))+1):
            t.fd(side)
            t.up()
            t.fd(2*side)
            t.down()
        t.up()
        t.setpos(-sizex/2+step,-sizey/2+step+step*(2*i+2))
        t.down()

def drawylinesfor61(x,step,angle):

    t=turtle.Turtle()
    turtle.tracer(0,0)
    t.speed(0)
    t.ht()
    t.up()
    t.setpos(x,sizey/2-step)
    t.right(angle)
    t.down()
    for i in range(int((sizex+(sizey-2*step)/math.sqrt(3))/step/3)):
        
        for j in range(int((sizey-2*step)*2/math.sqrt(3)/(3*side))+1):
            t.fd(side)
            t.up()
            t.fd(2*side)
            t.down()
        t.up()
        t.setpos(x+(3*i+1)*side,sizey/2-step)
        t.fd(side)
        t.down()
        for j in range(int(((sizey-2*step)*2/math.sqrt(3)-side)/(3*side))):
            t.fd(side)
            t.up()
            t.fd(2*side)
            t.down()
        t.up()
        t.setpos(x+side*(3*i+2),sizey/2-step)
        t.fd(2*side)
        t.down()
        for j in range(int(((sizey-2*step)*2/math.sqrt(3)-2*side)/(3*side))+1):
            t.fd(side)
            t.up()
            t.fd(2*side)
            t.down()
        t.up()
        t.setpos(x+side*(3*i+3),sizey/2-step)
        
        t.down()
def drawylinesfor62(x,step,angle):
    t=turtle.Turtle()
    turtle.tracer(0,0)
    t.speed(0)
    t.ht()
    t.up()
    t.setpos(x,sizey/2-step)
    t.right(angle)
    t.down()
    for i in range(int((sizex+(sizey-2*step)/math.sqrt(3))/step/3)):
        
        for j in range(int((sizey-2*step)*2/math.sqrt(3)/(3*side))+1):
            t.fd(side)
            t.up()
            t.fd(2*side)
            t.down()
        t.up()
        t.setpos(x+(3*i+1)*side,sizey/2-step)
        t.fd(2*side)
        t.down()
        for j in range(int(((sizey-2*step)*2/math.sqrt(3)-side)/(3*side))+1):
            t.fd(side)
            t.up()
            t.fd(2*side)
            t.down()
        t.up()
        t.setpos(x+side*(3*i+2),sizey/2-step)
        t.fd(side)
        t.down()
        for j in range(int(((sizey-2*step)*2/math.sqrt(3)-2*side)/(3*side))+1):
            t.fd(side)
            t.up()
            t.fd(2*side)
            t.down()
        t.up()
        t.setpos(x+side*(3*i+3),sizey/2-step)
        
        t.down()

def hexgrid():
    drawxlinesfor6(step)
    drawylinesfor61(-sizex/2+step-(sizey-2*step)/math.sqrt(3),step,60)
    drawylinesfor62(-sizex/2+step,step,120)
#hexgrid()

def limittriangle(size,cornerx,cornery):
    t=turtle.Turtle()
    t.up()
    turtle.tracer(0,0)
    x1,y1= cornerx,cornery
    t.setpos(x1,y1);t.down();t.dot(10);t.up()
    x2,y2=cornerx+size,cornery
    t.setpos(x2,y2);t.down();t.dot(10);t.up()
    t.lt(120)
    t.fd(size);t.down();t.dot(10);t.up()
    x3,y3=t.pos()
    centerx,centery=(x1+x2+x3)/3,(y1+y2+y3)/3
    random.seed();r1=random.random()
    #random.seed()
    r2=random.random()
    #random.seed();
    r3=random.random()
    print(r1,r2,r3)
    vx1,vx2,vx3=x1-centerx,x2-centerx,x3-centerx
    #print(vx1,vx2,vx3)
    vy1,vy2,vy3=y1-centery,y2-centery,y3-centery
    #print(vy1,vy2,vy3)
    startx,starty=centerx+(r1*vx1+r2*vx2+r3*vx3)/(r1+r2+r3),centery+(r1*vy1+r2*vy2+r3*vy3)/(r1+r2+r3)
    print(startx,starty)
    t.setpos(startx,starty)
    x,y=startx,starty
    for i in range(10**2):
        #t.up()
        x,y =(x+x1)/2,(y+y1)/2;t.setpos(x,y)
        t.down()
        t.dot(2)
        #t.up()
        x,y =(x+x2)/2,(y+y2)/2;t.setpos(x,y)
        t.down()
        t.dot(2)
        #t.up()
        x,y =(x+x3)/2,(y+y3)/2;t.setpos(x,y)
        #print(x,y)
        t.down()
        t.dot(2)
#limittriangle(600,-300,-300)
def limitsquare(size,cornerx,cornery):
    t=turtle.Turtle()
    t.up()
    turtle.tracer(0,0)
    x1,y1= cornerx,cornery
    t.setpos(x1,y1);t.down();t.dot(10);t.up()
    x2,y2=cornerx+size,cornery
    t.setpos(x2,y2);t.down();t.dot(10);t.up()
    t.lt(90)
    t.fd(size);t.down();t.dot(10);t.up()
    x3,y3=t.pos()
    t.lt(90)
    t.fd(size);t.down();t.dot(10);t.up()
    x4,y4=t.pos()
    centerx,centery=(x1+x2+x3+x4)/3,(y1+y2+y3+y4)/3
    random.seed();r1=random.random()
    #random.seed()
    r2=random.random()
    #random.seed();
    r3=random.random()
    r4=random.random()
    print(r1,r2,r3,r4)
    vx1,vx2,vx3,vx4=x1-centerx,x2-centerx,x3-centerx,x4-centerx
    #print(vx1,vx2,vx3)
    vy1,vy2,vy3,vy4=y1-centery,y2-centery,y3-centery,y4-centery
    #print(vy1,vy2,vy3)
    startx,starty=centerx+(r1*vx1+r2*vx2+r3*vx3+r4*vx4)/(r1+r2+r3+r4),centery+(r1*vy1+r2*vy2+r3*vy3+r4*vy4)/(r1+r2+r3+r4)
    print(startx,starty)
    t.setpos(startx,starty)
    x,y=startx,starty
    for i in range(10**2):
        #t.up()
        x,y =(x+x1)/2,(y+y1)/2;t.setpos(x,y)
        t.down()
        t.dot(2)
        #t.up()
        x,y =(x+x2)/2,(y+y2)/2;t.setpos(x,y)
        t.down()
        t.dot(2)
        #t.up()
        x,y =(x+x3)/2,(y+y3)/2;t.setpos(x,y)
        #print(x,y)
        t.down()
        t.dot(2)
        #t.up()
        x,y=(x+x4)/2,(y+y4)/2;t.setpos(x,y)
        t.down()
        t.dot(2)
#limitsquare(400,-300,-300)

def star(x,y,size,angle,vertices):
    #t=turtle.Turtle()
    t.speed(0)
    turtle.tracer(10**1,0)
    t.up();t.setpos(x,y);t.down()
    for i in range(0,vertices):
        t.fd(size)
        t.rt(angle)
def stars():
    t=turtle.Turtle()
    turtle.tracer(0,0)
    t.up();t.setpos(-600,320);t.down()
    size=432
    for k in range(7,10,1):
        #t.write(k, font=('Arial', 18, 'normal'))
        #t.up();t.rt(90);t.fd(20);t.lt(90)
        for i in range(2,k//2+1):
            if math.gcd(i,k)==1:
                star(t.xcor(),t.ycor(),size/(k)*i,i*360/k,k)
                t.up();t.rt(90);t.fd(size/2);t.lt(90);t.bk(size/(2*k));t.down()
        t.up();t.setpos(-600+(k-6)*size/2,320);t.down()
#stars()
def screen():
    #t.write(screensize())
    height=turtle.window_height()
    t.write(height)
    t.setpos(turtle.window_width()/2-10,turtle.window_height()/2-10)
#screen()
def starcenter(radius,centerx,centery,step,vertices):
    turtle.tracer(0,0)
    t.up()
    t.setpos(centerx,centery)
    x=[];y=[]
    for k in range(vertices):
        t.up();t.fd(radius)
        x.append(t.xcor());y.append(t.ycor())
        t.bk(radius);t.lt(360/vertices)
    #print(x)
    t.setpos(x[0],y[0])
    #t.color('yellow');t.dot()
    #turtle.bgcolor('black')
    #t.width(5)
    t.down()
    #step=2
    k=0
    color=['black','red','blue','orange','green','violet','yellow']
    num=0
    
    while k!=step:
        i=1;num+=1
        t.color(color[k%7])
        t.up();t.setpos(x[k%vertices],y[k%vertices]);t.down()
        t.setpos(x[(k+i*step)%vertices],y[(k+i*step)%vertices]);t.down()
        while t.pos()!=(x[k],y[k]):
            i+=1;num+=1
            t.setpos(x[(k+(step*i))%vertices],y[(k+(step*i))%vertices])
        if num!=vertices:
            k+=1
        elif num==vertices:
            k=step
        
    #turtle.tracer(0,0)
    t.up()

#t.up();t.setpos(-turtle.window_width()/2+1*size,turtle.window_height()/2-1*size)

def startable(low,high,width,size,starttype):
    t.width(width)
    for vertices in range(low,high):
        i=1
        for step in range(starttype,vertices//2+1):
            
            if 2*step!=vertices:
                
                if math.gcd(step,vertices)==1:
                    t.up();t.setpos(-turtle.window_width()/2+1*size+(2*size+3)*(vertices-low),turtle.window_height()/2-size-(2*size+5)*(i-starttype));t.down()
                    i+=1
                    if step==starttype:
                        t.up();t.sety(t.ycor()+size);t.color('black');t.write(vertices,align="left",font=("Arial",8,"normal"));t.sety(t.ycor()-size)
                    starcenter(size,t.xcor(),t.ycor(),step,vertices)
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
#t = turtle.Pen()

turtle.tracer(100,0)
turtle.bgcolor('black')
for x in range(360):
     t.pencolor(colors[x%6])
     t.width(x//100 + 1)
     t.forward(x)
     t.left(69)
start=time.time()
#startable(3,177,1,6,1)
end=time.time()
print(round(end-start,2))



turtle.exitonclick()
