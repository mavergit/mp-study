import tkinter
import turtle
import time
from turtle import *
import pyautogui
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
screen=pyautogui.screenshot()
screen.save("f1.png")


turtle.tracer(100,0)
turtle.speed(9)
top=(10*3**5)
t = turtle.Turtle()
t.color('green', 'yellow')

def draw1():
    start=time.time()
    for i in range(0,top):
        t.forward(15)
        t.left(i)
        if i==10:
            pass
            #color('green','green')
    print('time is ',time.time()-start)
#draw1()
def drawlines(size,step):
    i=0
    while i<=int(size/step):
        turtle.forward(size)
        turtle.penup()
        turtle.backward(size)
        turtle.left(90)
        turtle.forward(step)
        turtle.right(90)
        turtle.pendown()
        i+=1
def drawsquaregrid(size,step):
    drawlines(size,step)
    turtle.penup()
    turtle.left(90)
    turtle.backward(step)
    
    turtle.right(180)
    turtle.pendown()
    drawlines(size,step)
#turtle.stamp()
size=int(300)
#drawsquaregrid(size,10)
turtle.exitonclick()
