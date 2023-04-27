import random
import turtle as t

def route(screenSizeX: int, screenSizeY: int, hauteurRoute: int):
    """
    (fonction)
    route: create the road

    (variables)
    screenSizeX: the size of your screen in X in turtle
    screenSizeY: the size of your screen in Y in turtle
    hauteurRoute: the heigh of the road
    """
    SCREENMAXRIGHT = (screenSizeY / 2) * -1                             #on cree les constantes qui nous serons utiles pour plus tard
    SCREENMAXDOWN = (screenSizeX / 2) * -1
    SCREENMAXLEFT = screenSizeY / 2
    SCREENMAXUP = screenSizeX / 2
    LONGUEURTRAITS = 200
    HAUTEURTRAITS = 30
    HAUTEUROUTE = hauteurRoute

    def rectangle():                                                    #on cree la fonction pour faire les bandes de la route
        t.color("white")
        t.fillcolor("white")
        t.begin_fill()
        for i in range(2):
            t.forward(LONGUEURTRAITS)
            t.left(90)
            t.forward(HAUTEURTRAITS)
            t.left(90)
        t.end_fill()

    t.up()                                                              #on cree le rectangle noir qui nous sert de route
    t.goto(0,HAUTEUROUTE)
    t.down()
    t.goto(SCREENMAXRIGHT, HAUTEUROUTE)
    t.fillcolor("black")
    t.begin_fill()
    t.goto(SCREENMAXRIGHT, SCREENMAXDOWN)
    t.goto(SCREENMAXLEFT, SCREENMAXDOWN)
    t.goto(SCREENMAXLEFT, HAUTEUROUTE)
    t.goto(SCREENMAXRIGHT, HAUTEUROUTE)
    t.end_fill()

    t.penup()                                                           #on cree les bandes blanches 
    t.right(90)
    t.forward(((HAUTEUROUTE + SCREENMAXDOWN) / 2 + 100) * -1)
    t.left(90)
    t.forward(150)
    t.pendown()
    rectangle()
    t.penup()
    while (int(t.pos()[0]) < SCREENMAXLEFT):
        t.forward(HAUTEURTRAITS * 2 + 400)
        rectangle()

    t.color("grey")                                                     #on cree le trotoire de la route
    t.fillcolor("grey")
    t.begin_fill()
    t.goto(SCREENMAXLEFT, HAUTEUROUTE)
    t.goto(SCREENMAXLEFT, HAUTEUROUTE - 30)
    t.goto(SCREENMAXRIGHT, HAUTEUROUTE - 30)
    t.goto(SCREENMAXRIGHT, HAUTEUROUTE)
    t.goto(SCREENMAXLEFT, HAUTEUROUTE)
    t.end_fill()

    t.penup()
    t.goto(HAUTEUROUTE, 0)
    t.pendown()


if __name__ == "__main__":                              #on essaye si jamais on est pas dans un autre fichier
    SCREENSIZEX = 1080
    SCREENSIZEY = 1920
    HAUTEUROUTE = -100
    screen = t.Screen()
    screen.setup(SCREENSIZEY, SCREENSIZEX)
    route(SCREENSIZEX, SCREENSIZEY, HAUTEUROUTE)
    t.exitonclick()