from itertools import count
import turtle
from turtle import *
t=turtle.Turtle()
turtle.tracer(0,0)
countr=1
#global turtlerow,turtlecolumn

#рисуем поле

def draw_board():
    global cells,symbols
    global turtlerow,turtlecolumn
    global step,rows,columns
    t.color("green")
    #t.fd(400);t.bk(400);t.lt(90);t.fd(400);t.bk(400);t.rt(90)
    t.color("black")
    step=50
    rows=10;columns=10

    cells = [[0]]
    for j in range(rows): 
        cells.append([0])
        for i in range(columns-1):
            cells[j]+=[0]
    cells.remove([0])
    #print(cells)
    symbols=cells[:]
    print(symbols)
    sizes=[rows,columns]
    t.up();t.bk(step*columns/2)
    t.lt(90);t.fd(step*(rows/2-1));t.rt(90)
    for j in range(2):
        for i in range(sizes[j]-1):
            t.down()
            t.fd(step*sizes[(j+1)%2])
            t.up()
            t.rt(90*(-1)**(i+j*(rows%2-1)))
            t.fd(step)
            t.rt(90*(-1)**(i+j*(rows%2-1)))
        t.fd(step)
        t.rt(90*(-1)**rows)
    t.goto(0,0)
    cells[(rows-1)//2][(columns-1)//2]=0
    turtlecolumn=(rows+1)//2-1
    turtlerow=(columns+1)//2-1
    print(symbols[turtlerow][turtlecolumn])
    #print(cells)
    if columns%2==0:t.fd(25)
    if rows%2==0:t.lt(90);t.fd(25)

#двигаем черепашку
#def move_turtle():
#        global turtlerow,turtlecolumn
#        t.setheading(90)
def moveup():
    global turtlerow,turtlecolumn
    if t.ycor()<=step*rows/2-step:
        t.setheading(90)
        t.fd(step)
        turtle.update()
        turtlerow+=1
        print(turtlerow,turtlecolumn)

def movedown():
    global turtlerow,turtlecolumn
    if -t.ycor()<=rows/2*step-step:
        t.setheading(270)
        t.fd(step)
        turtle.update()
        turtlerow-=1
        print(turtlerow,turtlecolumn)

def moveleft():
    global turtlerow,turtlecolumn
    if -t.xcor()<=columns/2*step-step:
        t.setheading(180)
        t.fd(step)
        turtle.update()
        turtlecolumn-=1
        print(turtlerow,turtlecolumn)

def moveright():
    global turtlerow,turtlecolumn
    if t.xcor()<=columns/2*step-step:
        t.setheading(0)
        t.fd(step)
        turtle.update()
        turtlecolumn+=1
        print(turtlerow,turtlecolumn)



#ставим значок
t.width(2)
def set_symbol():
    global countr
    global symbols, turtlerow,turtlecolumn
    #print(turtlerow,turtlecolumn)

    if symbols[turtlerow][turtlecolumn]==0:
        if countr==1:
            t.down()
            t.width
            t.color("blue")
            t.rt(45);t.fd(step/2-2);t.bk(step-4);t.fd(step/2-2)
            t.rt(90);t.fd(step/2-2);t.bk(step-4);t.fd(step/2-2)
            t.lt(135)
            t.up()
            countr=0
            symbols[turtlerow][turtlecolumn]=1
            print(cells[turtlerow][turtlecolumn])
            turtle.update()
        elif countr==0:
            t.setheading(180)
            t.fd(step//3)
            t.lt(90)
            t.down()
            t.color("orange")
            t.circle(step//3,360,32)
            t.up()
            t.lt(90)
            t.fd(step//3)
            countr=1
            symbols[turtlerow][turtlecolumn]=2
            print(symbols[turtlerow][turtlecolumn])
            turtle.update()
    check_victory()



#проверяем 3 значка в ряд
def check_victory():
    global t,symbols,turtlerow,turtlecolumn
    def horizontal():
        global symbols,turtlerow,turtlecolumn
        for k in range(3):
            sum=0
            for j in range(3):
                sum+=symbols[turtlerow][turtlecolumn-k+j]
            if sum%3==0:
                t.write("hello")
                t.goto(0,0)
                return symbols[turtlerow][turtlecolumn]

        
    def vertical():
        global t, symbols,turtlerow,turtlecolumn

        for k in range(3):
            sum=0
            for j in range(3):
                sum+=symbols[turtlerow-k+j][turtlecolumn]
            if sum%3==0:
                return symbols[turtlerow][turtlecolumn]
                t.goto(0,0)
    
    def diagonal1():
        global symbols,turtlerow,turtlecolumn

        for k in range(3):
            sum=0
            for j in range(3):
                sum+=symbols[turtlerow-k+j][turtlecolumn-k+j]
            if sum%3==0:
                return symbols[turtlerow][turtlecolumn]
                t.goto(0,0)

    def diagonal2():
        global symbols,turtlerow,turtlecolumn

        for k in range(3):
            sum=0
            for j in range(3):
                sum+=symbols[turtlerow+k+j][turtlecolumn-k+j]
            if sum%3==0:
                return symbols[turtlerow][turtlecolumn]
                t.goto(0,0)
    
    horizontal()
    vertical()
    diagonal1()
    diagonal2()



onkeypress(moveup, "Up")
onkeypress(movedown, "Down")
onkeypress(moveleft, "Left")
onkeypress(moveright, "Right")
onkeypress(set_symbol, "space")
#основной цикл
def main():
    draw_board()
    turtle.update()
    turtle.listen()
    #move_turtle()
    turtle.update()
    turtle.mainloop()
main()

turtle.done()
