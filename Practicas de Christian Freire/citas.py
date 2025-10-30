import datetime
import os
import random

CARPETA = "usuarios/"  # Carpeta Usuarios
EXTENSION = ".txt"      # Extensión de Archivos



class App_citas:
    def __init__(self, nombre, apellido, fecha_nacimiento,edad, sexo, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.edad=edad
        self.cedula = cedula

def app():
    crear_directorio()  # Crear un directorio
    menu()     # Menú de citas Opciones
    
    pregunta = True     # Pregunta qué opción deseas elegir
    while pregunta:
        opcion = input("Elige una opción: \n")
        opcion = int(opcion)

        if opcion == 1:
            agregar_usuario()
            pregunta = False

        elif opcion == 2:
            editar_usuario()
            pregunta = False

        elif opcion == 3:
            eliminar_usuario()
            pregunta = False

        elif opcion == 4:
            formar_usuario_pareja()
            pregunta = False

        elif opcion == 5:
            ver_usuarios_sin_pareja()
            pregunta = False
        
        elif opcion == 6:
            exit()

        else:
            print("Opción no válida!")

def ver_usuarios_sin_pareja():
    usuarios_sin_pareja = []

    for archivo in os.listdir(CARPETA):
        if archivo.endswith(EXTENSION):
            contenido = open(CARPETA + archivo).read()
            if "Pareja:" not in contenido:
                usuarios_sin_pareja.append(archivo.split('.')[0])

    if usuarios_sin_pareja:
        print("Usuarios sin pareja:")
        for usuario in usuarios_sin_pareja:
            print(usuario)
    else:
        print("Todos los usuarios tienen pareja.")
    
    app()
        
def formar_usuario_pareja():
    print("Cargando parejas .....\n ")

    # Obtener la lista de usuarios masculinos y femeninos
    usuarios_masculinos = []
    usuarios_femeninos = []

    for archivo in os.listdir(CARPETA):
        if archivo.endswith(EXTENSION):
            with open(CARPETA + archivo, "r") as archivo_usuario:
                contenido = archivo_usuario.readlines()
                sexo = contenido[3].strip().split(": ")[1]

                if sexo.lower() == "masculino":
                    usuarios_masculinos.append(archivo)
                elif sexo.lower() == "femenino":
                    usuarios_femeninos.append(archivo)

    # si hay usuarios para hacer parejas
    if len(usuarios_masculinos) < 1 or len(usuarios_femeninos) < 1:
        print("No hay suficientes usuarios de ambos sexos para formar parejas.\n")
        app()
    # Forma parejas aleatorias
    parejas = []
    while usuarios_masculinos and usuarios_femeninos:
        usuario_masculino = random.choice(usuarios_masculinos)
        usuario_femenino = random.choice(usuarios_femeninos)

        parejas.append((usuario_masculino, usuario_femenino))

        # Eliminar usuarios emparejados de las listas
        usuarios_masculinos.remove(usuario_masculino)
        usuarios_femeninos.remove(usuario_femenino)

        # Muestra las parejas formadas
    if parejas:
        print("Aqui tienes las Parejas !!!:")
        for pareja in parejas:
            print(f"{pareja[0]} <--> {pareja[1]} \n ")
    else:
        print("No se pudieron formar parejas.\n")

    app()


def eliminar_usuario():
    print("Eliminar un usuario por número de Ci:")
    cedula_del_user = input("Ingresa el número Ci: del Usuario que deseas eliminar: \n")

    existe = existe_usuario(cedula_del_user)

    if existe:
        # Confirmar el Borrado
        confirmacion = input(f"¿Estás seguro de eliminar al usuario con Ci: {cedula_del_user}? (S/N): ").strip().lower()
        
        if confirmacion == "s":
            # Eliminar el archivo
            try:
                os.remove(CARPETA + cedula_del_user + EXTENSION)
                print(f"Usuario con CI: {cedula_del_user} eliminado !.")
            except OSError as e:
                print(f"No hay sistema, vuelva mañana: {str(e)}")
        else:
            print("Eliminación cancelada.")
    else:
        print("Esa Cédula no existe")

    app()

def editar_usuario():
    print("Editar datos de un usuario por número de cédula")
    cedula_edit_user = input("Ingresa el número de Cédula del Usuario que deseas editar: \n")
    
    existe = existe_usuario(cedula_edit_user)
    
    if existe:
        with open(CARPETA + cedula_edit_user + EXTENSION, "r") as archivo:
            contenido = archivo.readlines()
            
            # Obtener los datos actuales del usuario
            nombre_actual = contenido[0].strip().split(": ")[1]
            apellido_actual = contenido[1].strip().split(": ")[1]
            fecha_nacimiento_actual = contenido[2].strip().split(": ")[1]
            edad_actual=contenido[3].strip().split(": ")[1]
            sexo_actual = contenido[4].strip().split(": ")[1]
            
            # Pedir los nuevos datos o mantener los actuales
            nuevo_nombre = input(f"Nuevo Nombre del Usuario ({nombre_actual}): ") or nombre_actual
            while not nuevo_nombre or nombre_actual:
                print("Debe escribir un nombre")
                nuevo_nombre=input("Escriba el nombre del usuario: \n")
                
            nuevo_apellido = input(f"Nuevo Apellido del Usuario ({apellido_actual}): ") or apellido_actual
            while not nuevo_nombre or nombre_actual:
                print("Debe escribir el apellido")
                nuevo_nombre=input("Escriba el apellido del usuario: \n")
                
            nuevo_sexo = input(f"Nuevo Sexo del Usuario ({sexo_actual}): ") or sexo_actual
            while not nuevo_nombre or nombre_actual:
                print("Debe escribir un sexo")
                nuevo_nombre=input("Escriba el sexo del usuario: \n")
            
            nueva_fecha_nacimiento = input(f"Nueva fecha de nacimiento del usuario ({fecha_nacimiento_actual}): ") or fecha_nacimiento_actual
            while not nueva_fecha_nacimiento or not fecha_nacimiento_actual.count("-") == 2:
                print("El formato de fecha ingresado no es válido. Debe ser AAAA-MM-DD.")
                nueva_fecha_nacimiento = input("Agrega Fecha de Nacimiento del Usuario (AAAA-MM-DD): \n")
                
            nueva_fecha_nacimiento=datetime.datetime.strptime(nueva_fecha_nacimiento, '%Y-%m-%d')
            nueva_edad=datetime.datetime.now().year - nueva_fecha_nacimiento.year
            nueva_fecha_nacimiento = nueva_fecha_nacimiento.strftime('%Y-%m-%d')
            print("Su edad es: ",nueva_edad)
            if nueva_edad < 18:
                print("No puede ingresar es menor de edad.")
                menu()
            else:
                print("Sí puede ingresar.")
            # Actualizar los datos en el archivo
            contenido[0] = f"Nombre: {nuevo_nombre}\n"
            contenido[1] = f"Apellido: {nuevo_apellido}\n"
            contenido[2] = f"Fecha de Nacimiento: {nueva_fecha_nacimiento}\n"
            contenido[3] = f"Edad: {nueva_edad}\n"
            contenido[4] = f"Sexo: {nuevo_sexo}\n"
            
        with open(CARPETA + cedula_edit_user + EXTENSION, "w") as archivo_actualizado:
            archivo_actualizado.writelines(contenido)

        print("Datos del usuario actualizados exitosamente.")
    else:
        print("Esa cédula no existe")

    app()

def agregar_usuario():
    print("Escribe los datos para el Nuevo Usuario")
    cedula_usuario = input("Cédula del Usuario: \n")
    while not cedula_usuario:
            print("Debe escribir un número de cedula")
            cedula_usuario=input("Escriba el número de cedula del usuario: \n")

    # Revisar si el usuario ya existe antes de crearlo
    existe = existe_usuario(cedula_usuario)

    if not existe:
        with open(CARPETA + cedula_usuario + EXTENSION, "w") as archivo:

            # Resto de Campos
            nombre_usuario = input("Nombre del Usuario: \n")
            while not nombre_usuario:
                print("Debe escribir un nombre")
                nombre_usuario=input("Escriba el nombre del usuario: \n")
                
            apellido_usuario = input("Agrega el Apellido del Usuario: \n")
            while not apellido_usuario:
                print("Debe escribir un apellido")
                apellido_usuario=input("Escriba el apellido del usuario: \n")
            
            sexo_usuario = input("Agrega Sexo del Usuario: \n")
            while not sexo_usuario:
                print("Debe escribir un sexo")
                sexo_usuario=input("Escriba el sexo del usuario: \n")
            # Solicitar la fecha de nacimiento y validar el formato
            fecha_nacimiento_usuario = input("Agrega Fecha de Nacimiento del Usuario (AAAA-MM-DD): \n")
            while not fecha_nacimiento_usuario or not fecha_nacimiento_usuario.count("-") == 2:
                print("El formato de fecha ingresado no es válido. Debe ser AAAA-MM-DD.")
                fecha_nacimiento_usuario = input("Agrega Fecha de Nacimiento del Usuario (AAAA-MM-DD): \n")
            
            # Calcular la edad del usuario
            fecha_nacimiento_usuario=datetime.datetime.strptime(fecha_nacimiento_usuario, '%Y-%m-%d')   
            edad_usuario=datetime.datetime.now().year - fecha_nacimiento_usuario.year
            fecha_nacimiento_usuario = fecha_nacimiento_usuario.strftime('%Y-%m-%d')
            print("Su edad es:\r\n",edad_usuario)
            # Validar la edad (debe ser mayor o igual a 18)
            if edad_usuario < 18:
                print("No puede ingresar es menor de edad.")
                menu()
            else:
                print("Sí puede ingresar.")
                edad_usuario=str(edad_usuario)
                # Instanciar clase
                usuario = App_citas(nombre_usuario, apellido_usuario, fecha_nacimiento_usuario, edad_usuario, sexo_usuario, cedula_usuario)

                # Escribir la información en el archivo
                archivo.write("Nombre: " + usuario.nombre + "\n")
                archivo.write("Apellido: " + usuario.apellido + "\n")
                archivo.write("Fecha de Nacimiento: " + usuario.fecha_nacimiento + "\n")
                archivo.write("Edad: "+usuario.edad+"\n")
                archivo.write("Sexo: " + usuario.sexo + "\n")
                archivo.write("Cedula: " + usuario.cedula + "\n")

                print("\nUsuario Creado exitosamente\n")
    else:
        print("Ese Usuario ya existe")

    # Reiniciar la app
    app()


# menú de opciones de citas :3
def menu():
    print("Escoge una Opción en el menú:")
    print("1) Agregar Nuevo Usuario")
    print("2) Editar un Usuario")
    print("3) Eliminar Usuario")
    print("4) Formar Parejas")
    print("5) Ver Usuarios sin Pareja")
    print("6) Salir del sistema")

# crear el directorio si no existe
def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)

# si un usuario existe
def existe_usuario(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

# Iniciar la aplicación
app()