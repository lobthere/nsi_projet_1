import turtle
import random

if __name__ == "__main__":
    turtle.setup(1920, 1080)
    turtle.width(1)

def  route():
    hauteur_route = random.randint(100, 500)
    turtle.up()
    turtle.goto(-960, -540)
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

route()