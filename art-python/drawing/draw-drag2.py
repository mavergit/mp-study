from turtle import *
from turtle import Screen, Turtle

tur = Turtle()
tur.speed(0)
tracer(0,0)

def dragging(x, y): 
    tur.ondrag(None)
    tur.setheading(tur.towards(x, y))
    tur.goto(x, y)
    tur.ondrag(dragging)
    update()

def clear():
    tur.clear()
    update()

def main():  
    listen()
    tur.ondrag(dragging)  
    onscreenclick(clear, 2)
    onkey(clear,'c')
    update()
    mainloop()  

main()