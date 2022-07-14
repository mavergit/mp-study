#!/usr/bin/env python3
"""       turtle-example-suite:

            tdemo_paint.py

A simple  event-driven paint program

- left mouse button moves turtle
- middle mouse button changes color
- right mouse button toggles between pen up
(no line drawn when the turtle moves) and
pen down (line is drawn). If pen up follows
at least two pen-down moves, the polygon that
includes the starting point is filled.
 -------------------------------------------
 Play around by clicking into the canvas
 using all three mouse buttons.
 -------------------------------------------
          To exit press STOP button
 -------------------------------------------
"""
from turtle import *

screen=Screen()

def switchupdown(x=0, y=0):
    if pen()["pendown"]:
        end_fill()
        up()
    else:
        down()
        begin_fill()

def changecolor(x=0, y=0):
    global colors
    colors = colors[-1:]+colors[:-1]
    color(colors[0])
    #print(colors)

def reset():
    screen.reset()
    main()

#def setpoint(x=0,y=0):
#    circle(100)
    

def main():
    global colors
    shape("circle")
    resizemode("user")
    shapesize(.5)
    width(3)
    colors=["red", "green", "blue", "yellow"]
    color(colors[0])
    switchupdown()
    onscreenclick(goto,1)
    screen.onkey(changecolor,"space")
    onscreenclick(switchupdown,2)
    screen.onkey(reset,"c")
#    ondrag(setpoint,1)
    return "EVENTLOOP"

if __name__ == "__main__":
    msg = main()
    listen()
    print(msg)
    mainloop()