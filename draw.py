import turtle

painter = turtle.Turtle()
painter.pensize(10)

for _ in range(18):
    painter.forward(100)
    painter.left(100)

turtle.done()