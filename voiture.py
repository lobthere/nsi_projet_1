import turtle as voiture
 
def voiture1():
    # Code pour créer le fuselage de la voiture
    voiture.color('#008000')
    voiture.fillcolor('#008000')
    voiture.penup()
    voiture.begin_fill()
    voiture.forward(370)
    voiture.left(90)
    voiture.forward(50)
    voiture.left(90)
    voiture.forward(370)
    voiture.left(90)
    voiture.forward(50)
    voiture.end_fill()
    
    
    # Code pour créer les fenêtres de cette dernière
    voiture.penup()
    voiture.goto(100, 50)
    voiture.pendown()
    voiture.setheading(45)
    voiture.forward(70)
    voiture.setheading(0)
    voiture.forward(100)
    voiture.setheading(-45)
    voiture.forward(70)
    voiture.setheading(90)
    voiture.penup()
    voiture.goto(200, 50)
    voiture.pendown()
    voiture.forward(49.50)
    
    
    # Code pour créer les roues de cette automobile
    voiture.penup()
    voiture.goto(100, -10)
    voiture.pendown()
    voiture.color('#000000')
    voiture.fillcolor('#000000')
    voiture.begin_fill()
    voiture.circle(20)
    voiture.end_fill()
    voiture.penup()
    voiture.goto(300, -10)
    voiture.pendown()
    voiture.color('#000000')
    voiture.fillcolor('#000000')
    voiture.begin_fill()
    voiture.circle(20)
    voiture.end_fill()
