import turtle
import keyboard
#Configuracion inicial
t=turtle.Turtle("turtle#")
#Velocidad
t.speed(0)
#Fun. mover el dibujo
def mover_arriba():
    t.setheading(90)
    t.forward(10)

def mover_abajo():
    t.setheading(270)
    t.forward(10)

def mover_izquierda():
    t.setheading(180)
    t.forward(10)

def mover_derecha():
    t.setheading(0)
    t.forward(10)


#Habilitar teclas
keyboard.add_hotkey("w",mover_arriba)
keyboard.add_hotkey("s",mover_abajo)
keyboard.add_hotkey("a",mover_izquierda)
keyboard.add_hotkey("d",mover_derecha)

#Mantener la ventana abierta
turtle.mainloop()