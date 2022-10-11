from turtle import *
from random import *

speed(2)
def immeuble(largeur):
    def facade():
        fillcolor("red")
        begin_fill()
        for i in range (2) :
            forward(largeur)
            left(90)
            forward(largeur)
            left(90)
        end_fill()
    facade()
    def nb_etages():
            for nb_etages in range(3) :
                left(90)
                forward(largeur)
                right(90)
                facade()
    nb_etages()




immeuble(100)