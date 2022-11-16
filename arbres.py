import turtle as arbre

TREESIZEY = 370
TREESIZEX = 50
LEAVSSIZE = 250

def arbres(treeSizeY, treeSizeX, leavesSize):
    '''here is the trunk of the tree'''
    arbre.color("brown")
    arbre.fillcolor('brown')
    arbre.penup()
    arbre.begin_fill()
    arbre.forward(treeSizeX)
    arbre.left(90)
    arbre.forward(treeSizeY)
    arbre.left(90)
    arbre.forward(treeSizeX)
    arbre.left(90)
    arbre.forward(treeSizeY)
    arbre.end_fill()

    '''Here are the leaves of the tree'''
    arbre.color('green')
    arbre.fillcolor('green')
    arbre.penup()

    """here we turn"""
    arbre.forward(treeSizeY * -1)
    arbre.left(90)
    arbre.forward(((leavesSize - treeSizeX) / 2) * -1)
    arbre.pendown()

    arbre.begin_fill()
    for i in range(4):
        arbre.forward(leavesSize)
        arbre.left(90)
    arbre.end_fill()

arbres(TREESIZEY, TREESIZEX, LEAVSSIZE)