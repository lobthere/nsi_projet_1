import turtle as t
from random import randint, random
from route import route
from arbres import arbres
from immeuble import immeuble
from case_creole import case
from voiture import voiture1
import time

"""Init"""
t.bgpic("test/0 (1).png")
t.speed(100000000000)
t.hideturtle()
t.title("Un jour une ville")
COLOR = [0, 0, 0]

"""About the Screen"""
SCREENSIZEY = 1920
SCREENSIZEX = 1080
SCREENMAXRIGHT = (SCREENSIZEY / 2) * -1
SCREENMAXDOWN = (SCREENSIZEX / 2) * -1
SCREENMAXLEFT = SCREENSIZEY / 2
SCREENMAXUP = SCREENSIZEX / 2

"""About the Road"""
HAUTEUROUTE = -100

"""About the Tree"""
TREESIZEY = 100
TREESIZEX = 20
LEAVSSIZE = 50
NUMBER_OF_TREES = 6

"""About the Building"""
SCREEN_SIZE_BUILDING_X = 100
NUMBEROFETAGES = 2
COLOR_FACADE = [0, 0, 0]
COLOR_WINDOW1 = [0, 0, 0]
COLOR_WINDOW2 = [0, 0, 0]

"""About the Case"""
CASESIZE = 100
ROOFSIZE = 50
COLOR_CASE = [0, 0, 0]

"""About the Car"""
COLOR_CAR = [0, 0, 0]

"""The fonctions"""
def immeuble_in_main():
    NUMBEROFETAGES = randint(2, 4)
    COLOR_FACADE = choose_color(COLOR)
    COLOR_WINDOW1 = choose_color(COLOR)
    COLOR_WINDOW2 = choose_color(COLOR)
    immeuble(SCREEN_SIZE_BUILDING_X, NUMBEROFETAGES, COLOR_FACADE, COLOR_WINDOW1, COLOR_WINDOW2)

def arbre_in_main():
    t.goto(SCREENMAXRIGHT, HAUTEUROUTE - 30)
    for i in range(0, NUMBER_OF_TREES, 1):
        t.forward(randint(LEAVSSIZE + 100, LEAVSSIZE + 500) )
        t.pendown()
        arbres(TREESIZEY, TREESIZEX, LEAVSSIZE)
        t.penup()

def choose_color(color):
    color = [randint(0, 255), randint(0, 255), randint(0, 255)]
    return color

screen = t.Screen()
screen.setup(SCREENSIZEY, SCREENSIZEX)
route(SCREENSIZEX, SCREENSIZEY, HAUTEUROUTE)

"""The build"""

t.penup()
t.goto(SCREENMAXRIGHT, HAUTEUROUTE)
t.pendown()
t.color("black")
random = 0
while (t.pos()[0]) < SCREENMAXLEFT:
    random = randint(1, 2)
    COLOR_CASE = choose_color(COLOR)
    if random == 1:
        immeuble_in_main()
        t.forward(SCREEN_SIZE_BUILDING_X * 2)
    elif random == 2:
        case(CASESIZE, ROOFSIZE, COLOR_CASE)
        t.forward(CASESIZE)

t.penup()
arbre_in_main()

t.goto(randint(-800, 800), HAUTEUROUTE - 300)
COLOR_CAR = choose_color(COLOR)
voiture1(COLOR_CAR)
number = 0
while number != 587:
    number = number + 1
    t.bgpic(f"test/0 ({number}).png")
    screen.update()
    time.sleep(0.03)
t.exitonclick()