import turtle as t
from route import route
from arbres import arbres
from voiture import voiture1

"""About the Screen"""
SCREENSIZEY = 1920
SCREENSIZEX = 1080

"""About the Road"""
HAUTEUROUTE = -100

"""About the Tree"""
TREESIZEY = 370
TREESIZEX = 50
LEAVSSIZE = 250

screen = t.Screen()
screen.setup(SCREENSIZEY, SCREENSIZEX)
route(SCREENSIZEX, SCREENSIZEY, HAUTEUROUTE)

t.goto(HAUTEUROUTE, -100)
arbres(TREESIZEY, TREESIZEX, LEAVSSIZE)

t.exitonclick()