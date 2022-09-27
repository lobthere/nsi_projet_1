from turtle import *
import debut
import toit
import carre

debut.debut()
taille = 50

carre.carre(taille, "red")

left(90)
penup()
fd(taille)
right(90)
pendown()

toit.toit(taille, "blue")