import turtle

def draw_turtle(side):   
    for k in range(4):
        turtle.fd(side)
        turtle.lt(90)
        
draw_turtle(100)

turtle.rt(90)
turtle.fd(100)

def draw_turtle(side):   
    for k in range(8):
        turtle.fd(side)
        turtle.lt(45)
        
draw_turtle(100)

turtle.done()