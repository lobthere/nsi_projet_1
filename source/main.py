import turtle as t
from random import randint, random
from route import route
from arbres import arbres
from immeuble import immeuble
from case_creole import case
from voiture import voiture1
import time

"""Init"""
t.bgpic("timelaps/0 (1).png")                       #Ajoute l'image en fond
t.speed(100000000000)                               #met la vitesse de la tortue au maximum
t.hideturtle()                                      #cache la tortue
t.title("Un jour une ville")                        #set le nom de la fenetre
COLOR = [0, 0, 0]                                   #initialise le format de couleur

"""About the Screen"""
SCREENSIZEY = 1920                                  #definie les dimensions de la fenetre
SCREENSIZEX = 1080
SCREENMAXRIGHT = (SCREENSIZEY / 2) * -1
SCREENMAXDOWN = (SCREENSIZEX / 2) * -1
SCREENMAXLEFT = SCREENSIZEY / 2
SCREENMAXUP = SCREENSIZEX / 2

"""About the Road"""
HAUTEUROUTE = -100                                  #definie la hauteur de la route

"""About the Tree"""
TREESIZEY = 100                                     #definie les dimensions ainsi que la taille des arbres
TREESIZEX = 20
LEAVSSIZE = 50
NUMBER_OF_TREES = 6

"""About the Building"""
SCREEN_SIZE_BUILDING_X = 100                        #definie la taille des building, le nombre d'etages par default ainsi que le format necessaire pour la couleur
NUMBEROFETAGES = 2
COLOR_FACADE = [0, 0, 0]
COLOR_WINDOW1 = [0, 0, 0]
COLOR_WINDOW2 = [0, 0, 0]

"""About the Case"""
CASESIZE = 100                                      #definie la taille de la case créole
ROOFSIZE = 50
COLOR_CASE = [0, 0, 0]

"""About the Car"""
COLOR_CAR = [0, 0, 0]                               #definie la couleur de la voiture

"""The fonctions"""
def immeuble_in_main():                             #crée la fonction qui vas choisir toutes la variables aleatoire necessaire pour construire 
    NUMBEROFETAGES = randint(2, 4)                  #l'immeuble mais aussi le construire
    COLOR_FACADE = choose_color(COLOR)
    COLOR_WINDOW1 = choose_color(COLOR)
    COLOR_WINDOW2 = choose_color(COLOR)
    immeuble(SCREEN_SIZE_BUILDING_X, NUMBEROFETAGES, COLOR_FACADE, COLOR_WINDOW1, COLOR_WINDOW2)        #on appelle la fonction du fichier immeuble

def arbre_in_main():                                #on va a la position predefinie et on crée un nombre d'arbre predefinie
    t.goto(SCREENMAXRIGHT, HAUTEUROUTE - 30)
    for i in range(0, NUMBER_OF_TREES, 1):
        t.forward(randint(LEAVSSIZE + 100, LEAVSSIZE + 500) )
        t.pendown()
        arbres(TREESIZEY, TREESIZEX, LEAVSSIZE)
        t.penup()

def choose_color(color):                                                #fonction qui sert a choisir aleatoirement les couleurs pour toutes les fonctions
    color = [randint(0, 255), randint(0, 255), randint(0, 255)]
    return color

screen = t.Screen()                                                     #initialise l'ecran
screen.setup(SCREENSIZEY, SCREENSIZEX)                                  #cree la fenetre avec les dimensions
route(SCREENSIZEX, SCREENSIZEY, HAUTEUROUTE)                            #cree la route avec les parametres predefinie

"""The build"""

t.penup()                                                               #fonction principal ou on va construire les batiments et les maisons
t.goto(SCREENMAXRIGHT, HAUTEUROUTE)                                     #dans un ordre tiree au hasard
t.pendown()
t.color("black")
random = 0
while (t.pos()[0]) < SCREENMAXLEFT:                                     #la fonction qui crée les batiments et les maisons
    random = randint(1, 2)                                              #on choisit aléatoirement si c'est une maison ou un batiment
    COLOR_CASE = choose_color(COLOR)                                    #on choisit une couleur 
    if random == 1:                                                     #si c'est 1 on fait un immeuble
        immeuble_in_main()
        t.forward(SCREEN_SIZE_BUILDING_X * 2)
    elif random == 2:                                                   #si c'est 2 on fait une case
        case(CASESIZE, ROOFSIZE, COLOR_CASE)                            #on utilise la fonction case du fichier case
        t.forward(CASESIZE)

t.penup()
arbre_in_main()                                                         #on cree les arbres a partir du fichier arbres.py

t.goto(randint(-800, 800), HAUTEUROUTE - 300)                           
COLOR_CAR = choose_color(COLOR)
voiture1(COLOR_CAR)                                                     #on cree la voiture
number = 0
while number != 587:                                                    #la boucle qui permet de faire le timelaps
    number = number + 1                                                 #on incremente la variable number
    t.bgpic(f"timelaps/0 ({number}).png")                               #on selectionne la photo a partir du fichier 
    screen.update()                                                     #on fait une mise a jour d'ecran 
    time.sleep(0.03)                                                    #on attent 0.03s
t.exitonclick()                                                         #pour partir a la fin en cliquant sur la fenetre