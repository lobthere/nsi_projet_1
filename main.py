import turtle as t
from route import route
from arbres import arbres
from voiture import voiture1

SCREENSIZEY = 1920
SCREENSIZEX = 1080
HAUTEUROUTE = -100

screen = t.Screen()
screen.setup(SCREENSIZEY, SCREENSIZEX)
route(SCREENSIZEX, SCREENSIZEY, HAUTEUROUTE)

t.goto(HAUTEUROUTE, -100)
arbres()

t.exitonclick()