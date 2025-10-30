#Iniciar un diccionario vacío
jugador={}
print(jugador)

#Se une un nuevo jugador
jugador["Nombre"]="Christian"
jugador["Puntaje"]=0
print(jugador)

#Incrementando el puntaje
jugador["Puntaje"]=1000
print(jugador)

#Acceder a un valor
print(jugador.get("Consola","No existe ese valor"))

#Iterar el diccionario
for llave,valor in jugador.items():
    print(valor)
    
#Eliminar jugador y puntaje
del jugador["Nombre"]
del jugador["Puntaje"]
print(jugador)