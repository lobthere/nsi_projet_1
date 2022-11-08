from turtle import *
from random import *
hideturtle()
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
        def fenetre():
            up()
            fillcolor("white")
            forward(largeur/5)
            left(90)
            begin_fill()
            forward(largeur/4)
            right(90)
            forward(largeur/6)
            left(90)
            forward(largeur/6)
            left(90)
            forward(largeur/6)
            left(90)
            forward(largeur/6)
            end_fill()
            forward(largeur/4)
            left(270)
            forward(largeur/5)
            left(180)
            down()
            
        fenetre()
    facade()
    def porte():
        forward(largeur/2)
        fillcolor("brown")
        begin_fill()
        left(90)
        forward(largeur/2)
        right(90)
        forward(largeur/4)
        right(90)
        forward(largeur/2)
        right(90)
        forward(largeur/4)
        end_fill()
        forward(largeur/2)  
        right(180) 
    porte()
    def nb_etages():
            for nb_etages in range(2) :
                left(90)
                forward(largeur)
                right(90)
                facade()
    nb_etages()

    return immeuble

immeuble(100)

exitonclick()