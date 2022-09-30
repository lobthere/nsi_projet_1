from turtle import *
from carre import *

def fenetre():
    """
    tracer la fenetre
    """
    up()
    goto(0, 0)
    fd(cote/4)
    left(90)
    fd(cpte/4)
    down()
    for i in range(0, 4, 1) :
        fd(carre.cote/4)
        left(90)

carre(4, "red")
fenetre()