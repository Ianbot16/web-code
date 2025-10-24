import math
import turtle
turtle.bgcolor("black")
turtle.shape("turtle")
turtle.speed(0)
turtle.goto(0,-40)
turtle.pendown()
#Usando el angulo dorado
phi= 137.508 * (math.pi / 180.0)
for j in range(18):
    turtle.color("yellow")
    turtle.rt(90)
    #Dibuja el primer medio circulo
    turtle.circle(150 - j * 6, 90)
    turtle.lt(90)
    #Dibuja el otro medio circulo
    turtle.circle(150 - j * 6, 90)
turtle.penup()
turtle.goto(0,0)
turtle.color("black")
turtle.done()