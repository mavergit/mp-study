import turtle
import random
import math

turtle.tracer(20,0)
def create_turtles():
    global t,vx,vy,m,fx,fy,monitor,num
    t=[]
    num=10**2 #number of turtles
    vx=[];vy=[] #initial velocities
    m=[]
    fx=[];fy=[]
    for i in range(num):
        t.append(turtle.Turtle())
        t[-1].up() 
        t[-1].setpos(random.randrange(0,400)-200,random.randrange(0,400)-200)
        t[-1].fd(100)
        vx.append(random.randrange(-1,1))
        #vx.append(0)
        vy.append(random.randrange(-1,1))
        #vy.append(0)
        m.append(random.randrange(1,5))
        t[-1].turtlesize(m[-1],m[-1])
        fx.append(0)
        fy.append(0)
    monitor=turtle.Turtle()
    monitor.ht()
    monitor.fd(250)

#def move(turtle):
def force(distance):
    const=1
    f=const/(distance**2)
    return f
def main_loop():
    while 1:
        kinenergy=0
        for k in range(len(t)):
            fx[k]=0
            fy[k]=0
            
            for j in range(len(t)):

                if j==k:
                    continue
                dkj=t[k].distance(t[j]) #! change to tor surface geometry
                fx[k]+=(t[j].xcor()-t[k].xcor())/(dkj**0.5)*force(dkj)
                fy[k]+=(t[j].ycor()-t[k].ycor())/(dkj**0.5)*force(dkj)
            vx[k]+=fx[k]/m[k]
            vy[k]+=fy[k]/m[k]
            t[k].setx((t[k].xcor()+vx[k]+200)%400-200)
            t[k].sety((t[k].ycor()+vy[k]+200)%400-200)
            
            kinenergy+=m[k]/2*(vx[k]+vy[k])

            #t[k].setpos((t[k].xcor()+t[(k+2)%len(t)].xcor())/2,(t[k].ycor()+t[(k+2)%len(t)].ycor())/2)
        monitor.clear()
        monitor.write(round(kinenergy,2))
        turtle.update()

def main():
    create_turtles()
    main_loop()

main()


turtle.done()