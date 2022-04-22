from turtle import Turtle
import turtle
import time
turtle.tracer(1,0)

screen=turtle.Screen()

t0=turtle.Turtle()
for i in range(100):
    pass
    #t0.fd(10)
    #t0.rt(10)
    #turtle.delay(1000)
    #time.sleep(1)

#val=turtle.textinput("val", "Input value")
#print(val)

def func1():
    t0.fd(10)

def func2():
    t0.circle(50)

turtle.onkey(func1,"Right")
turtle.onscreenclick(t0.goto)
#turtle.onclick(None)

turtle.listen()

turtle.update()
turtle.mainloop()