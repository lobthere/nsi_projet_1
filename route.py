import turtle
import random

def  route():
    hauteur_route = random.randint(100, 500)
    turtle.up()
    turtle.goto(-x/2, -y/2)
    turtle.down()
    turtle.color("black")
    turtle.fillcolor("black")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(1080*2)
        turtle.left(90)
        turtle.forward(hauteur_route)
        turtle.left(90)
    turtle.end_fill()
    turtle.up()
    turtle.goto(0 ,0)
    turtle.color("white")
    turtle.down()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(-100)
        turtle.left(90)
    turtle.end_fill()


x = 1920
y = 1080

if __name__ == "__main__":
    turtle.setup(x, y)
    turtle.width(1)


route()