from cmath import tan
import turtle as t
from random import randint

def case (SIZE: int, HEIGHT_TOIT: int, color):
    """
    (fonction): make a case creole

    (variable): 
    SIZE : choose the size of the house
    HEIGHT_TOIT: choose the height of the roof
    color: choose the color of the house
    """
    t.colormode(255)
    t.color(color[0], color[1], color[2])
    t.fillcolor(color[0], color[1], color[2])
    t.begin_fill()
    for i in range(0 ,4, 1):
        t.forward(SIZE)
        t.left(90)
    t.end_fill()

    t.forward(SIZE / 2 - 10)
    t.color('black')

    t.fillcolor("brown")
    t.begin_fill()
    t.left(90)
    t.forward(40*SIZE/100)
    t.right(90)
    t.forward(20*SIZE/100)
    t.right(90)
    t.forward(40*SIZE/100)
    t.end_fill()
    t.fillcolor(color[0] % 2, color[1], color[2])

    t.left(90)
    t.forward(-((SIZE/2-10) + 20*SIZE/100))

    t.left(90)
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
