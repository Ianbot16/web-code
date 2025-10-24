import turtle
def dibujar_rombo():
    window = turtle.Screen()
    window.bgcolor("black")
    rombo=turtle.Turtle()
    rombo.shape("turtle")
    rombo.speed(10)
    rombo.color("yellow")
    for _ in range(2):
        rombo.forward(100)
        rombo.right(60)
        rombo.forward(100)
        rombo.right(120)
    window.exitonclick()
dibujar_rombo()