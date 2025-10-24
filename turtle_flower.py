import turtle
def dibuja_flor():
    window = turtle.Screen()
    window.bgcolor("black")
    flor = turtle.Turtle()
    flor.shape("turtle")
    flor.speed(10)
    flor.color("yellow")
    for _ in range(36):
        for _ in range(2):
            flor.forward(100)
            flor.right(60)
            flor.forward(100)
            flor.right(120)
        flor.right(10)
    flor.right(90)
    flor.color("green")
    flor.forward(300)
    window.exitonclick()
dibuja_flor()