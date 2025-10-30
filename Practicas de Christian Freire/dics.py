#Creando un diccionario simple
cancion={
    "Artista":"Bon Jovi",
    "Canción":"Livin on Prayer",
    "Año": 1987,
    "Likes": 300000
}

#Accediendo a los elementos del diccionario
print(cancion["Artista"])

#Mezclar un string
artista= cancion["Artista"]
print(f"Estoy escuchando a {artista}.")

#Creando nuevos elementos
cancion["Playlist"] ="Rock"
print(cancion)

#Reemplazar valor existente
cancion["Canción"]="Runaway"
print(cancion)

#Eliminar un valor
del cancion["Año"]
print(cancion)