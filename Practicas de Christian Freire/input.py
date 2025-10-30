#nombre=input("Cúal es tu nombre: \r\n")

#print(f"Hola {nombre}")

#Ingresar la edad y verificar que pueda votar
edad=input("Cúal es tu edad: \r\n")
#Convertir string a entero
edad=int(edad)
if edad >= 18:
    print("Ya puedes votar")
else:
    print("Aún no puedes votar")


#Mezclar número con operadores
numero=int(input("Ingresa un número y yo te diré si es par o impar: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")