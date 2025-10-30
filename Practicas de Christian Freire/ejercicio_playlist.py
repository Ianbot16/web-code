playlist={}
playlist['canciones']=[]#Lista vacia de canciones

#Funciones principales
def app():
    #Agrgar playlist
    agregar_playlist=True

    while agregar_playlist:
        nombre_playlist=input("¿Como deseas nombrar la playlist? \r\n")
        if nombre_playlist:
            playlist["nombre"]=nombre_playlist
            #Ya tenemos el nombre, desactivar la playlist
            agregar_playlist=False
            #Mandar a llamar la función para agragar canciones.
            agregar_canciones()

def agregar_canciones():
    #Bandera para agregar canciones
    agregar_canciones=True
    while agregar_canciones:
        #Preguntar al usuario que canción desea agregar
        nombre_playlist=playlist["nombre"]
        pregunta=f"\r\nAgregar canciones para la playlist {nombre_playlist} \r\n"
        pregunta+="Escribe una X para dejar de escribir canciones: "

        cancion=input(pregunta)

        if cancion == "X":
            #Dejar de agregar canciones
            agregar_canciones=False
            mostrar_resumen()
        else:
            #Agregando canciones a la playlist
            playlist["canciones"].append(cancion)
            print(playlist)

def mostrar_resumen():
    nombre_playlist=playlist["nombre"]
    print(f"Playlist: {nombre_playlist}\r\n")
    print("Canciones: \r\n")
    for cancion in playlist["canciones"]:
        print(cancion)

app()