from turtle import *
from random import *

def immeuble(largeur: int, nb: int, color_facade: list, color_fenetre1: list, color_fenetre2: list):
    """
    (fonction)
    immeuble : make the building using turtle

    (variables)
    largeur :       the width of the building
    nb:             the number of stage
    color_facade:   the color of the front
    color_fenetre1: the color of the first windows
    color_fenetre2: the color of the second windows
    """
    colormode(255)                              #choisit le color mode pour le rgb
    def facade():                               #cree la facade
        fillcolor(color_facade)
        begin_fill()
        for i in range (2) :
            forward(largeur*2)
            left(90)
            forward(largeur)
            left(90)
        end_fill()
        
        def fenetre():                          #cree la fenetre numero 1
            up()
            fillcolor(color_fenetre1)
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

        def fenetre2():                         #cree la fenetre numero 2
            up()
            forward(largeur+largeur/2)            
            fillcolor(color_fenetre2)
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
            forward(largeur/2)
            forward(largeur/2)
            forward(largeur/2)
            forward(largeur/5)
            left(180)
            down()
        fenetre()                           #on appelle les fonctions fenetres
        fenetre2()
    position = [pos()[0], pos()[1]]         #on sauvegarde la position de la tortue
    facade()                                #on fait la facade
    def porte():                            #on cree la fonction pour la porte
        forward(largeur)
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
        forward(largeur)  
        right(180) 
    porte()                                 #on appelle la fonction porte et la cree
    def nb_etages():                        #on definie en fonction du nombre d'etage la fonction
            for nb_etages in range(nb - 1) :
                left(90)
                forward(largeur)
                right(90)
                facade()
    nb_etages()                             #on cree le nombre d etage requis
    goto(position[0], position[1])          #on vas a la position sauvegardee plus tot
    return largeur                          #on renvoie la largeur