from turtle import *
from turtle import Turtle, Screen

def drag(x, y):
    t1.ondrag(True)
    t1.setheading(t1.towards(x, y))
    t1.goto(x, y)
    #t2.setheading(t2.towards(t1))
    #t2.fd(1)
    t2.goto((t2.xcor()*9/10+t1.xcor()*1/10),(t2.ycor()*9/10+t1.ycor()*1/10))
    update()
    t1.ondrag(drag)


tracer(0,0)

t1 = Turtle('turtle')
t1.speed(0)
t2=Turtle('turtle')
t2.color('red')
t2.width(3)
t2.speed(0)
t2.fd(100)

def main():
    listen() 
    t1.ondrag(drag)
    update()
    done()

main()