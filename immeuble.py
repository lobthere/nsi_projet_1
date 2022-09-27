from turtle import *
from random import *

HAUTEUR_SOUS_PLAFOND = 100

def immeuble(pos_x, pos_y, largeur):
    up()
    goto(pos_x, pos_y)
    down()
    goto(pos_x + largeur, pos_y)
    goto(pos_x + largeur, pos_y + HAUTEUR_SOUS_PLAFOND)
    goto(pos_x, pos_y + HAUTEUR_SOUS_PLAFOND)
    goto(pos_x, pos_y)
    
    
immeuble(-200, -100, 100)


