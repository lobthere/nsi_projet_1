from cmath import tan
import turtle as t
from random import randint

def case (SIZE: int, HEIGHT_TOIT: int, color: list):
    """
    (fonction): make a case creole

    (variable): 
    SIZE : choose the size of the house
    HEIGHT_TOIT: choose the height of the roof
    color: choose the color of the house
    """
    t.colormode(255)                                    #definie le colormode pour le rgb
    t.color(color[0], color[1], color[2])               #saisie la couleur choisit aleatoirement
    t.fillcolor(color[0], color[1], color[2])           #choisit la couleur de fond
    t.begin_fill()                                      #on commence a remplir
    for i in range(0 ,4, 1):                            #on cree les 4 coins de la maison
        t.forward(SIZE)
        t.left(90)
    t.end_fill()                                        #on arrete de remplir

    t.forward(SIZE / 2 - 10)                            #on avance de la variable size definie 
    t.color('black')                                    #on change la couleur en noir

    t.fillcolor("brown")                                #on choisit la couleur de fond marron
    t.begin_fill()                                      #on commence a remplir
    t.left(90)                                          #on cree la porte
    t.forward(40*SIZE/100)
    t.right(90)
    t.forward(20*SIZE/100)
    t.right(90)
    t.forward(40*SIZE/100)
    t.end_fill()
    t.fillcolor(color[0] % 2, color[1], color[2])

    t.left(90)
    t.forward(-((SIZE/2-10) + 20*SIZE/100))

    t.left(90)                                          #on cree le toit en considerant qu il est isocele
    t.forward(SIZE)
    t.right(90)
    position_1 = [t.pos()[0], t.pos()[1]]
    t.penup()
    t.forward(SIZE / 2)
    t.left(90)
    t.forward(HEIGHT_TOIT)
    position_2 = [t.pos()[0], t.pos()[1]]
    t.goto(position_1[0], position_1[1])
    t.pendown()
    t.begin_fill()
    t.goto(position_2[0], position_2[1])
    t.goto(position_1[0] + SIZE, position_1[1])
    t.goto(position_1[0], position_1[1])
    t.end_fill()
    t.left(180)
    t.forward(SIZE)
    t.left(90)