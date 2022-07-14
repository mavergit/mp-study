import turtle
t1=turtle.Turtle()
s1=turtle.Screen()

def changecolor(x=0, y=0):
    global colors
    colors = colors[1:]+colors[:1]
    t1.color(colors[0])
    #print(colors)

def switchupdown(x=0, y=0):
    if t1.pen()["pendown"]:
        t1.end_fill()
        t1.up()
    else:
        t1.down()
        t1.begin_fill()


def reset():
    t1.clear()


def main():
    turtle.listen()
    global colors
    t1.shape("circle")
    t1.resizemode("user")
    t1.shapesize(.5)
    t1.width(3)
    colors=["red", "green", "blue", "yellow"]
    t1.color(colors[0])
    switchupdown()
    turtle.onscreenclick(t1.goto,1)
    turtle.onkey(changecolor,"space")
    s1.onclick(switchupdown,2)
    turtle.onkey(reset,"c")
    return "EVENTLOOP"
    

main()

turtle.mainloop()



