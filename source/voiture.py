import turtle as t
 
def voiture1(color: list):
    """
    (fonction)
    voiture1: create the car 

    (variables)
    color: choose the color for the car, need to be a list [color1, color2, color3]
    """
    t.colormode(255)

    # Code pour créer le fuselage de la voiture
    t.color(color)
    t.fillcolor(color)
    t.penup()
    t.begin_fill()
    t.forward(370)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(370)
    t.left(90)
    t.forward(50)
    t.end_fill()
    t.left(90)
    
    
    # Code pour créer les fenêtres de cette dernière
    t.penup()
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.pendown()
    t.setheading(45)
    t.forward(70)
    t.setheading(0)
    t.forward(100)
    t.setheading(-45)
    t.forward(70)
    t.setheading(90)
    t.penup()
    t.right(90)
    t.forward(-100)
    t.pendown()
    t.left(90)
    t.forward(49.50)    
    
    # Code pour créer les roues de cette automobile
    t.penup()
    t.forward(-108.99)
    t.right(90)
    t.forward(-1 * (99.5 + 10))
    t.pendown()
    t.color("red")
    t.fillcolor("red")
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()
    t.forward(300 - 89.49)
    t.pendown()
    t.color("red")
    t.fillcolor("red")
    t.begin_fill()
    t.circle(20)
    t.end_fill()