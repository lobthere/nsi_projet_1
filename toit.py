from turtle import *
from random import *

def toit(taille: int, couleur):
    """
    taille: taille du toit
    couleur: couleur du toit
    pos_x: position du toit
    """
    ht()
    pu()
    pd()
    color(couleur)
    fillcolor(couleur)
    begin_fill()
    c =0
    while c < 3:
        forward(taille)
        right(-120)
        c = c +1
    end_fill()