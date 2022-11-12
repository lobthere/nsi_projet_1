from turtle import *
import random


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
