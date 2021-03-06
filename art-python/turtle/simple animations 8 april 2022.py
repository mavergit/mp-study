import tkinter
import turtle
import time
import math
import random

sizex = 1280
sizey = 720
ww = turtle.window_width()
wh = turtle.window_height()
turtle.setup(width=sizex, height=sizey, startx=0, starty=0)
turtle.tracer(0, 0)
turtle.colormode(255)


t = turtle.Turtle()
t.speed(0)
t.ht()
t.width(3)
t0 = turtle.Turtle()
t0.speed(0)
# t.ht()
t0.width(3)
t.up()
t.setpos(0, 0)
t.down()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t2.up()
t2.setpos(-540, 230)
t2.down()
t3.up()
t3.setpos(-540, -230)
t3.down()


def drawcircle(t, radius):
    # t.up();
    t.fd(radius)
    t.lt(90)
    t.down()
    t.circle(radius)
    # t.up();
    t.rt(90)
    t.bk(radius)
    t.down()


def drawsquare(t, radius):
    t.fd(radius)
    t.lt(90)
    t.fd(radius)
    t.lt(90)
    for i in range(3):
        t.fd(2 * radius)
        t.lt(90)
    t.fd(radius)
    t.rt(90)
    t.bk(radius)


def rotate_square(t, radius):
    angle = 1
    while True:
        drawsquare(t, radius)
        turtle.update()
        t.clear()
        t.rt(1)
        # time.sleep(1)


def rotate_wheel(t, radius):
    angle = 1
    while True:
        drawcircle(t, radius)
        turtle.update()
        t.clear()
        t.rt(1)


def animate_wheel():
    t.up()
    t.setpos(-540, 0)
    t.down()
    radius = 100
    steps = 1800
    shift = 1
    angle = shift / (radius * 2 * math.pi) * 360
    i = 0
    while True:

        # turtle.bgcolor(i%255,i%255,i%255)
        drawcircle(t, radius)
        drawcircle(t2, radius)
        drawcircle(t3, radius)
        t.lt(angle * i)
        t.up()
        t.fd(shift)
        t.down()
        t.rt(angle * (i + 1))
        t2.lt(5 * angle * i)
        t2.up()
        t2.fd(shift)
        t2.down()
        t2.rt(5 * angle * (i + 1))
        t3.lt(0.2 * angle * i)
        t3.up()
        t3.fd(shift)
        t3.down()
        t3.rt(0.2 * angle * (i + 1))
        turtle.update()

        t.clear()
        t2.clear()
        t3.clear()
        i += 1


def horizbounce_wheel():
    t.up()
    t.setpos(-240, 0)
    t.down()
    t2.up()
    t2.setpos(-240, 200)
    t2.down()
    t3.up()
    t3.setpos(-240, -200)
    t3.down()
    radius = 100
    steps = 360
    # shift=1
    # angle=shift/(radius*2*math.pi)*360
    angle = 1
    shift = angle * radius * 2 * math.pi / 360
    i = 0
    while True:
        for i in range(360):
            # turtle.bgcolor(i%255,i%255,i%255)
            drawcircle(t, radius)
            drawcircle(t2, radius)
            drawcircle(t3, radius)
            t.lt(angle * i)
            t.up()
            t.fd(shift)
            t.down()
            t.rt(angle * (i + 1))
            t2.lt(5 * angle * i)
            t2.up()
            t2.fd(shift)
            t2.down()
            t2.rt(5 * angle * (i + 1))
            t3.lt(0.2 * angle * i)
            t3.up()
            t3.fd(shift)
            t3.down()
            t3.rt(0.2 * angle * (i + 1))
            turtle.update()

            t.clear()
            t2.clear()
            t3.clear()

        for i in range(360):
            # turtle.bgcolor(i%255,i%255,i%255)
            drawcircle(t, radius)
            drawcircle(t2, radius)
            drawcircle(t3, radius)
            t.rt(angle * i)
            t.up()
            t.bk(shift)
            t.down()
            t.lt(angle * (i + 1))
            t2.rt(5 * angle * i)
            t2.up()
            t2.bk(shift)
            t2.down()
            t2.lt(5 * angle * (i + 1))
            t3.rt(0.2 * angle * i)
            t3.up()
            t3.bk(shift)
            t3.down()
            t3.lt(0.2 * angle * (i + 1))
            turtle.update()
            t.clear()
            t2.clear()
            t3.clear()


def toothtri(t, r, num, x1, x2, y1, y2):
    a = t.distance(x1, y1)
    t.up()
    t.goto(x1, y1)
    t.down()
    t.rt(60)
    t.fd(a)
    t.lt(120)
    t.fd(a)
    t.rt(60)


def tooth(t, r, num, x1, x2, y1, y2):
    a = t.distance(x1, y1)
    t.rt(90)
    t.circle(-a / 2, 180)
    t.rt(90)


def gear(r, teeth):

    num = 2 * teeth
    xcor = []
    ycor = []
    for i in range(teeth):

        t0.circle(r, 360 / num)
        xcor.append(t0.xcor())
        ycor.append(t0.ycor())
        t0.up()
        t0.circle(r, 360 / num)
        xcor.append(t0.xcor())
        ycor.append(t0.ycor())
        t0.down()
        tooth(t0, r, num, xcor[-2], xcor[-1], ycor[-2], ycor[-1])
        t0.up()
        t0.circle(r, 360 / num)
        t0.down()


# animate_wheel()
# rotate_wheel(t,200)
# rotate_square(t,200)
# horizbounce_wheel()

# gear(150,20)
my_dict = {}


for i in range(10 ** 3):
    x = str(i)
    my_dict[x] = turtle.Turtle()

    my_dict[x].rt(random.randrange(360))
    my_dict[x].fd(400)
turtle.update()
turtle.exitonclick()
