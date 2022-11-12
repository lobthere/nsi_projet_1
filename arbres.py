import turtle as arbre


def arbre():
    '''here is the trunk of the tree'''
    arbre.color("brown")
    arbre.fillcolor('brown')
    arbre.penup()
    arbre.goto(0,-300)
    arbre.begin_fill()
    arbre.forward(50)
    arbre.left(90)
    arbre.forward(370)
    arbre.left(90)
    arbre.forward(50)
    arbre.left(90)
    arbre.forward(370)
    arbre.end_fill()

    '''Here are the leaves of the tree'''
    arbre.color('green')
    arbre.fillcolor('green')
    arbre.penup()
    arbre.goto(-100,200)
    arbre.begin_fill()
    arbre.forward(250)
    arbre.left(90)
    arbre.forward(250)
    arbre.left(90)
    arbre.forward(250)
    arbre.left(90)
    arbre.forward(250)
    arbre.left(90)
    arbre.forward(250)
    arbre.end_fill()