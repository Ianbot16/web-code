#Realiza un examén con 3 preguntas que tu desees, el usuario deberá responder "Sí" o "No" y al final otorgarle una calificación
# (La calificación se logra con una variable que inicia en 0 y por cada respuesta correcta incrementa en 1)
print("Responda las siguientes preguntas.")
numero_correcto=0

primera_pregunta=input("Si María tiene 10 manzanas en su canasta, y le da 3 a sus amigos, ¿Tendría María 5 manzanas? S/N \r\n")
if primera_pregunta == "N":
    print("Respuesta Correcta")
    numero_correcto+=1
else:
    print("Respuesta Incorrecta")
    
segunda_pregunta=input("Si Juan tiene 25 canicas y las divide entre sus 4 amigos. ¿Le tocaría a Juan 5 canicas? S/N \r\n")
if segunda_pregunta == "S":
    print("Respuesta Correcta")
    numero_correcto+=1
else:
    print("Respuesta Incorrecta")
    
tercera_pregunta=input("Si Marta tiene un cuaderno de 100 hojas y arranca 40 hojas. ¿Tendría Marta 50 hojas aún en su cuaderno? S/N \r\n")


if tercera_pregunta == "N":
    print("Respuesta Correcta")
    numero_correcto+=1
else:
    print("Respuuesta Incorrecta")
    
print(f"Respondistes {numero_correcto} preguntas correctas")