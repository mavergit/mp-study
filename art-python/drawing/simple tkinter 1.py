from tkinter import *
window = Tk()
window.geometry("960x720")

def paint(event):
    x1,y1=event.x-1,event.y-1
    x2,y2=event.x,event.y
    color="blue"
    canvas.create_oval(x1,y1,x2,y2,fill=color,outline=color)

canvas = Canvas(window, bg='white')
canvas.bind('<B1-Motion>',paint)
#canvas.pack()
canvas.pack(anchor='nw', fill='both', expand=1)

window.mainloop()