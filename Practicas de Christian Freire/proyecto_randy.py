import os

CARPETA = "contactos/"  # Carpeta Contact
EXTENSION = ".txt"      # Extensión de Archivos


class Contactos:
    def __init__(self, nombre, cell, categoria):
        self.nombre = nombre
        self.cell = cell
        self.categoria = categoria


def app():

    crear_directorio()  # Revisa si existe o no
    ver_menu()          # Ver Menú de Opciones

    pregunta = True     # Pregunta qué opción deseas elegir
    while pregunta:
        opcion = input("Elige una opción: \r\n ")
        opcion = int(opcion)

        if opcion == 1:
            agg_contacto()
            pregunta = False

        elif opcion == 2:
            edit_contacto()
            pregunta = False

        elif opcion == 3:
            ver_contacto()
            pregunta = False

        elif opcion == 4:
            print("Buscar Contacto ")
            pregunta = False

        elif opcion == 5:
            print("Eliminar Contacto ")
            pregunta = False

        else:
            print("Opción no válida!")


def ver_contacto():
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    
    for archivo in archivos_txt:
        with open(CARPETA+ archivo) as contacto:
            for linea in contacto:
                # Ver los contenidos
                print(linea.lstrip())
                # seperador entre cada contacto
            print ("\r\n")

    app()



def edit_contacto():
    print("Contacto a editar")
    name_anterior = input("Nombre del contacto para editarlo: \r\n")

    # Revisar si el contacto ya existe antes de editarlo
    existe = existe_contacto(name_anterior)

    if existe:
        with open(CARPETA + name_anterior + EXTENSION, "w") as archivo:
            # Resto de los campos
            name_contacto = input("Agrega el Nuevo Nombre del Contacto: \r\n")
            cell_contacto = input("Agrega el Nuevo Teléfono: \r\n")
            categoria_contacto = input("Agrega la Nueva Categoría del Contacto: \r\n")

            # Instanciar
            contacto = Contactos(name_contacto, cell_contacto, categoria_contacto)

            # Escribir en el Archivo
            archivo.write("Nombre: " + contacto.nombre + "\r\n")
            archivo.write("Cell: " + contacto.cell + "\r\n")
            archivo.write("Categoria: " + contacto.categoria + "\r\n")

            # Reescribir el Archivo
            os.rename(CARPETA + name_anterior + EXTENSION, CARPETA + name_contacto + EXTENSION)

    else:
        print("Ese contacto no existe")

    app()


def agg_contacto():
    print("Escribe los datos Para el Nuevo Contacto")
    name_contacto = input("Nombre del Contacto: \r\n")

    # Revisar si el contacto ya existe antes de crearlo
    existe = existe_contacto(name_contacto)

    if not existe:
        with open(CARPETA + name_contacto + EXTENSION, "w") as archivo:

            # Resto de Campos
            cell_contacto = input("Agrega el Teléfono: \r\n")
            categoria_contacto = input("Categoría del Contacto: \r\n")

            # Instanciar clase
            contacto = Contactos(name_contacto, cell_contacto, categoria_contacto)

            archivo.write("Nombre: " + contacto.nombre + "\r\n")
            archivo.write("Cell: " + contacto.cell + "\r\n")
            archivo.write("Categoria: " + contacto.categoria + "\r\n")

            print("\r\nContacto Creado exitosamente \r\n")

    else:
        print("Ese Contacto ya existe")

    # Reiniciar la app
    app()


def ver_menu():
    print("Escoge una Opción en el menú:")
    print("1) Agregar Nuevo Contacto")
    print("2) Editar Contacto")
    print("3) Ver Contacto")
    print("4) Buscar Contacto")
    print("5) Eliminar Contacto")


def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)


def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()