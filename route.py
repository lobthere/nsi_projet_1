import turtle as t
import random

SCREENSIZEX = 600
SCREENSIZEY = 900
SCREENMAXRIGHT = (SCREENSIZEY / 2) * -1
SCREENMAXDOWN = (SCREENSIZEX / 2) * -1
SCREENMAXLEFT = SCREENSIZEY / 2
SCREENMAXUP = SCREENSIZEX / 2
HAUTEUROUTE = -100

screen = t.Screen()
screen.setup(SCREENSIZEY, SCREENSIZEX)
t.up()
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

t.penup()
t.right(90)
t.forward(((SCREENMAXDOWN + HAUTEUROUTE) / 2 + 30) * -1)
t.left(90)
t.forward(200)
t.pendown()
t.color("red")
t.forward(20)
t.exitonclick()
