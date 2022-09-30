from turtle import *
import debut

def carre(cote, couleur):
    down()
    color(couleur)
    fillcolor(couleur)
    begin_fill()

    for i in range(0, 4, 1):
        fd(cote)
        left(90)
    end_fill()