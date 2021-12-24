#%%
import tkinter
import time
#from rich import print
import turtle
from turtle import *
turtle.tracer(100,0)
turtle.speed(0)
#color1=input("chose color")
#color("#554433")
#color('#{color1}')

start=time.time()
top=2*360
for i in range(0,top-1):
    turtle.forward(i*10**(-2))
    left(i)
forward((top-1)*10**2/10**4)
print(speed, " -> ", time.time()-start)
turtle.exitonclick()

# %%
