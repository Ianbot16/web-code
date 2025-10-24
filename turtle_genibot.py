import turtle
def dibujar_genibot():
    turtle.shape("circle")
    for _ in range(4):             #Se repetira 4 veces
        turtle.forward(150)
        turtle.left(90)
    turtle.penup()
    turtle.goto(30,100)      #Posicion del primer cuadro
    turtle.pendown()               #Baja el lapiz del cursor
    turtle.fillcolor("black")      #Color del relleno del dibujo
    turtle.begin_fill()            #Comienza a rellenar el area
    for _ in range(2):             #Dibuja el ojo como rectangulo
        turtle.forward(15)         #mueve el cursor 15 px
        turtle.left(90)            #Gira 90° a la izquierda
        turtle.forward(30)         #Mueve el cursor 30 px
        turtle.left(90)            #Gira el cursor 30 px
    turtle.end_fill()              #Gira el cursor a la izquierda
    turtle.penup()                 #Finaliza el llenado del área
dibujar_genibot()                  #Levanta nuevamente el lapiz
turtle.done()