import turtle as t
from route import route
from arbres import arbres
from immeuble import immeuble

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
TREESIZEY = 370
TREESIZEX = 50
LEAVSSIZE = 250

"""About the Building"""
SCREEN_SIZE_BUILDING_X = 100
NUMBEROFETAGES = 2

screen = t.Screen()
screen.setup(SCREENSIZEY, SCREENSIZEX)
route(SCREENSIZEX, SCREENSIZEY, HAUTEUROUTE)

t.penup()
t.goto(HAUTEUROUTE, -100)
t.pendown()
arbres(TREESIZEY, TREESIZEX, LEAVSSIZE)

t.penup()
t.goto(SCREENMAXRIGHT, HAUTEUROUTE)
t.pendown()
immeuble(SCREEN_SIZE_BUILDING_X, NUMBEROFETAGES)

t.exitonclick()