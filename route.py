from turtle import *
import random

if __name__ == "__main__":
    setup(1920, 1080)
    width(1)

def  route():
    hauteur_route = random.randint(100, 500)
    up()
    goto(-960, -540)
    down()
    color("black")
    fillcolor("black")
    begin_fill()
    for i in range(2):
        forward(1080*2)
        left(90)
        forward(hauteur_route)
        left(90)
    end_fill()

route()