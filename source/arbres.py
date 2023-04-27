import turtle as arbre

def arbres(treeSizeY: int, treeSizeX: int, leavesSize: int):
    '''
    (fonction)
    arbres : make a tree for you using turtle 
    
    (variables)
    treeSizeY  : the height of your trunk
    treeSizeX  : the size of your trunk
    leavesSize : the size of your leavs
    '''

    '''here is the trunk of the tree'''
    position = [arbre.pos()[0], arbre.pos()[1]]                                     #on sauvegarde la position actuel de l'arbre
    arbre.color("brown")                                                            #on cree le tronc
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

    '''Here are the leaves of the tree'''                                           #on cree les feuilles
    arbre.color('green')
    arbre.fillcolor('green')
    arbre.penup()

    """here we turn"""
    arbre.forward(treeSizeY * -1)
    arbre.left(90)
    arbre.forward(treeSizeX/2)
    arbre.right(90)
    arbre.forward(treeSizeX/2)
    arbre.left(90)
    arbre.pendown()
    arbre.begin_fill()
    arbre.circle(leavesSize)
    arbre.end_fill()
    arbre.penup()
    arbre.goto(position[0], position[1])                                            #on retourne a la position sauvegarder au paravant
    arbre.forward(treeSizeX / 2)
    arbre.pendown()

if __name__ == "__main__":                                                          #permet d'essayer le programme avec des valeurs par default 
    TREESIZEY = 370
    TREESIZEX = 50
    LEAVSSIZE = 100
    arbres(TREESIZEY, TREESIZEX, LEAVSSIZE)