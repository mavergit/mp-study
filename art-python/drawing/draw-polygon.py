import turtle

window = turtle.Screen()
fred = turtle.Turtle()

def draw_polygon(n_sides):
    fred.clear()
    for _ in range(n_sides):
        fred.forward(400 / n_sides)
        fred.left(360 / n_sides)

for n in range(3, 10):
    window.onkeypress(lambda n=n: draw_polygon(n), str(n))

window.listen()

turtle.done()