import os

CARPETA="contactos/" #Carpeta de contactos
EXTENSION=".txt" #Extensión de archivos

#Contactos
class Contacto:
    def __init__(self,nombre,telefono,categoria):
        self.nombre=nombre
        self.telefono=telefono
        self.categoria=categoria
        
        
def app():
    #Revisar si la carpeta existe
    crear_directorio()
    
    #Muestra el menú de opciones
    mostrar_menu()
    
    #Pregunta al usuario la acción a realizar
    preguntar=True
    while preguntar:
        opcion=input("Seleccione una opción: \r\n")
        opcion=int(opcion)
        
        #Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar=False
        elif opcion == 2:
            editar_contacto()
            preguntar=False
        elif opcion == 3:
            mostrar_contacto()
            preguntar=False
        elif opcion == 4:
            buscar_contacto()
            preguntar=False
        elif opcion == 5:
            eliminar_contacto()
            preguntar=False
        else:
            print("Opción no válida, intente de nuevo.")

def eliminar_contacto():
    nombre= input("Seleccione el contacto que desea eliminar: \r\n")
    
    try:
        os.remove(CARPETA+nombre+EXTENSION)
        print("Contacto eliminado correctamente")
    
    except:
        print("No existe ese contacto")
    
    app()

def buscar_contacto():
    nombre= input("Seleccione el contacto que desea buscar: \r\n")
    
    try:
        with open(CARPETA+nombre+EXTENSION) as contacto:
            print("\r\nInformación del Contacto: \r\n")
            for linea in contacto:
                print(linea.lstrip())
                print("\r\n")
    
    except IOError:
        print("El archivo no existe")
        print(IOError)
    
    app()
    
def mostrar_contacto():
    archivos = os.listdir(CARPETA)
    
    archivos_txt= [i for i in archivos if i.endswith(EXTENSION)]
    
    for archivo in archivos_txt:
        with open(CARPETA+archivo) as contacto:
            #Imprime los contactos en linea
            for linea in contacto:
                print(linea.lstrip())
            #Imprimir un separador de contactos
            print("\r\n")
    
    app()
    
def editar_contacto():
    print("Escribe el nombre del contacto a editar")
    nombre_anterior=input("Escriba el nombre del contacto que desea editar: \r\n")
    
    #Revisar si el archivo ya existe antes de crearlo
    existe=existe_contacto(nombre_anterior)
    
    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, "w") as archivo:
           #Resto de los campos
            nombre_contacto=input("Agrega el nuevo nombre: \r\n")
            telefono_contacto=input("Agregar el nuevo teléfono: \r\n")
            categoria_contacto=input("Agrega la nueva categoría: \r\n")
         
           #Instanciar
            contacto=Contacto(nombre_contacto,telefono_contacto,categoria_contacto)
            
           #Escribir en el archivo
            archivo.write("Nombre: "+ contacto.nombre + "\r\n")
            archivo.write("Teléfono: "+ contacto.telefono + "\r\n")
            archivo.write("Categoria: "+ contacto.categoria + "\r\n")
            
            
            #Renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
            #Mostrar mensaje de exito
            print("r\n\ Contacto editado correctamente \r\n")
    else:
        print("Ese contacto no existe")
    
    app()
      
def agregar_contacto():
    print("Escribe los datos para agregar el Contacto")
    nombre_contacto=input("Nombre del Contacto:\r\n")
    
    #Revisar si el archivo ya existe antes de crearlo
    existe=os.path.isfile(CARPETA + nombre_contacto + EXTENSION)
    
    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, "w") as archivo:
        #Resto de los campos
         telefono_contacto=input("Agregar el teléfono: \r\n")
         categoria_contacto=input("Categoría del contacto: \r\n")
        
        #Instanciar las clases
         contacto=Contacto(nombre_contacto,telefono_contacto,categoria_contacto)
        
        #Escribir en el archivo
         archivo.write("Nombre: "+ contacto.nombre + "\r\n")
         archivo.write("Teléfono: "+ contacto.telefono + "\r\n")
         archivo.write("Categoria: "+ contacto.categoria + "\r\n")
        
        #Mostrar mensaje de exito
         print("r\n\ Contacto creado correctamente \r\n")
    
    else:
        print("Ese contacto ya existe")
    
    #Reiniciar la app
    app()


    
        
def mostrar_menu():
    print("Seleccione del Menú lo que desea hacer: ")
    print("1) Agregar nuevo contacto")
    print("2) Editar Contactos")
    print("3) Ver Contactos")
    print("4) Buscar Contacto")
    print("5) Eliminar Contacto")

        
def crear_directorio():
    if not os.path.exists(CARPETA):
        #Crear carpeta
        os.makedirs(CARPETA)
    
def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)
            
    

app()