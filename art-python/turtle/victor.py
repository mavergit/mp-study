from itertools import count
from lib2to3.pygram import Symbols
import turtle
from turtle import *
t=turtle.Turtle()
turtle.tracer(0,0)
countr=1
pobeda=3
#рисуем поле
def draw_board():
    global step,rows,columns
    global cells
    t.color("green")
    #t.fd(400);t.bk(400);t.lt(90);t.fd(400);t.bk(400);t.rt(90)
    t.color("black")
    step=50
    rows=10;columns=10
    cells = [[2]]
    for j in range(rows): 
        for i in range(columns-1):
            cells[j]+=[2]
        cells.append([2])
    cells.remove([2])
    #print(cells)
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
    if columns%2==0:t.bk(25)
    if rows%2==0:t.rt(90);t.fd(25)

#двигаем черепашку
def move_turtle():
    t.setheading(90)
    global tcolumn,trow
    trow=rows//2
    tcolumn=columns//2
    if not rows%2==0:trow+1
    if not columns%2==0:tcolumn+1
    def up():
        global tcolumn,trow
        if t.ycor()<=rows/2*step-step: 
            t.setheading(90)
            t.fd(step)
            turtle.update()
            trow=trow+1

    def down():
        global tcolumn,trow
        if -t.ycor()<=rows/2*step-step:
            t.setheading(270)
            t.fd(step)
            turtle.update()
            trow=trow-1

    def left():
        global tcolumn,trow
        if -t.xcor()<=columns/2*step-step:
            t.setheading(180)
            t.fd(step)
            turtle.update()
            tcolumn=tcolumn-1

    def right():
        global tcolumn,trow
        if t.xcor()<=columns/2*step-step:
            t.setheading(0)
            t.fd(step)
            turtle.update()
            tcolumn=tcolumn+1

    onkeypress(up, "Up")
    onkeypress(down, "Down")
    onkeypress(left, "Left")
    onkeypress(right, "Right")
    onkeypress(set_symbol, "space")
        
#ставим значок
def set_symbol():
    t.width(2)    
    global countr,tcolumn,trow,cells
    if cells[trow][tcolumn]==2:
        if countr==1:
            cells[trow][tcolumn]=1
            t.down()
            t.color("blue")
            t.rt(45);t.fd(step/2-2);t.bk(step-4);t.fd(step/2-2)
            t.rt(90);t.fd(step/2-2);t.bk(step-4);t.fd(step/2-2)
            t.lt(135)
            t.up()
            turtle.update()
            check_victory()
            countr=0

        elif countr==0:
            cells[trow][tcolumn]=0
            t.setheading(180)
            t.fd(step/3+5)
            t.lt(90)
            t.down()
            t.color("orange")
            t.circle(step/3+5,360,32)
            t.up()
            t.lt(90)
            t.fd(step/3+5)
            turtle.update()
            check_victory()
            countr=1
        
#проверяем 3 значка в ряд
def check_victory():
    global tcolumn,trow,cells,countr,pobeda,vryad,b
    def vertical():
        global tcolumn,trow,cells,countr,pobeda,vryad1,b
        b=0
        print(b)
        vryad1=0
        vryad2=0
        while not (cells[trow-b][tcolumn]==(2 or countr)):
            vryad1+=1
            print(vryad1)
            b+=1
            
        while not (cells[trow+b][tcolumn]==(2 or countr)):
            vryad2+=1
            print(vryad2)
            b+=1
            #print(b)
        
        if vryad1+vryad2==pobeda:
            t.down()
            t.color("red")
            #t.write("hi")
            t.write("ура",font=('Arial',18,'normal'))
            
            t.up()
        elif vryad1+vryad2<pobeda:    
            diogonal1()
        

    def gorizantal():
        global tcolumn,trow,cells,countr
        vertical()

    def diogonal1():
        global tcolumn,trow,cells,countr
        diogonal2() 

    def diogonal2():
        pass
    vertical()

#основной цикл
def main():
    draw_board()
    turtle.update()
    turtle.listen()
    move_turtle()
    turtle.update()
    turtle.mainloop()
main()

turtle.done()
