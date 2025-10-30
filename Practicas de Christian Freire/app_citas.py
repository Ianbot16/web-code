import datetime
import os

CARPETA="citas/" #La carpeta dondé se almacenarán las citas
EXTENSION=".txt" #La extensión

#App de citas
class App_citas:
    #Creando los datos personales
    def __init__(self,cedula,nombres,apellidos,fecha_nacimiento,edad,sexo,) -> None:
        self.cedula=cedula
        self.nombres=nombres
        self.apellidos=apellidos
        self.fecha_nacimiento=fecha_nacimiento
        self.edad=edad
        self.sexo=sexo
        

def app():
    crear_directorio()
    #Mostrar el menú con opciones
    mostrar_menu()

    #Creando el menú
    preguntar=True
    while preguntar:
        opcion=int(input("Elija una opción: \r\n"))
        if opcion==1:
            agregar_cita()
            preguntar=False
            
        elif opcion==2:
            editar_cita()
            preguntar=False
            
        elif opcion==3:
            buscar_cita()
            preguntar=False
            
        elif opcion==4:
            unir_cita()
            preguntar=False
        
        elif opcion==5:
            mostrar_cita()
            preguntar=False
            
        elif opcion==6:
            eliminar_cita()
            preguntar=False
            
        elif opcion==7:
            break
        else:
            print("Incorrecto, escriba otro número")
        
    
def agregar_cita():
    print("Escribe los datos a ingresar")
    cedula_cita=input("Ingrese su número de cédula: \r\n")
    
    #Revisar si el archivo ya existe antes de crearlo
    existe=os.path.isfile(CARPETA + cedula_cita + EXTENSION)
    
    if not existe:
        with open(CARPETA + cedula_cita + EXTENSION, "w") as archivo:
        #Resto de los campos
            nombres_cita=input("Ingrese sus nombres: \r\n")
            apellidos_cita=input("Ingrese sus apellidos: \r\n")
            fnacimiento_cita=input("Ingrese su fecha de nacimiento (YYYY-MM-DD): \r\n")
            fnacimiento_cita=datetime.datetime.strptime(fnacimiento_cita, '%Y-%m-%d')
            edad_cita=datetime.datetime.now().year - fnacimiento_cita.year
            fnacimiento_cita = fnacimiento_cita.strftime('%Y-%m-%d')
            print("Su edad es: \r\n", edad_cita)
            edad_cita=str(edad_cita)
            if edad_cita == "18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60":
                print("No puede ingresar es menor de edad")
                
            else:
                print("Si puede ingresar")
            
            sexo_cita=input("Ingrese su sexo (Masculino o Femenino): \r\n")
        
        
            #Instanciar las clases
            citas=App_citas(cedula_cita,nombres_cita,apellidos_cita,fnacimiento_cita,edad_cita,sexo_cita)
            
            #Escribir en el archivo
            archivo.write("Cedula: "+ citas.cedula + "\r\n")
            archivo.write("Nombres: "+ citas.nombres + "\r\n")
            archivo.write("Apellidos: "+ citas.apellidos + "\r\n")
            archivo.write("Fecha de nacimiento: "+ citas.fecha_nacimiento + "\r\n")
            archivo.write("Edad: "+ citas.edad + "\r\n")
            archivo.write("Sexo: "+ citas.sexo + "\r\n")
        
        #Mostrar mensaje de exito
        print("Cita creada correctamente \r\n")
    
    else:
        print("Esa cita ya existe")
        

    #Reiniciar la app
    app()

def editar_cita():
    print("Escribe la cedula del contacto a editar")
    cedula_cita=input("Escriba la cedula del contacto que desea editar: \r\n")
    
    #Revisar si el archivo ya existe antes de crearlo
    existe=existe_citas(cedula_cita)
    
    if existe:
        with open(CARPETA + cedula_cita + EXTENSION, "w") as archivo:
           #Resto de los campos
            nombres_cita=input("Agrega los nuevos nombres: \r\n")
            apellidos_cita=input("Agrega los nuevos apellidos: \r\n")
            fnacimiento_cita=input("Ingrese su fecha de nacimiento (YYYY-MM-DD): \r\n")
            fnacimiento_cita=datetime.datetime.strptime(fnacimiento_cita, '%Y-%m-%d')
            edad_cita=datetime.datetime.now().year - fnacimiento_cita.year
            fnacimiento_cita = fnacimiento_cita.strftime('%Y-%m-%d')
            print("Su edad es: \r\n", edad_cita)
            edad_cita=str(edad_cita)
            if edad_cita == "18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60":
                print("No puede ingresar es menor de edad")
            else:
                print("Si puede ingresar")
            sexo_cita=input("Ingrese su sexo (Masculino o Femenino): \r\n")
         
           #Instanciar
            citas=App_citas(cedula_cita,nombres_cita,apellidos_cita,fnacimiento_cita,edad_cita,sexo_cita)
            
           #Escribir en el archivo
           
            archivo.write("Cedula: "+ citas.cedula +"\r\n")
            archivo.write("Nombres: "+ citas.nombres + "\r\n")
            archivo.write("Apellidos: "+ citas.apellidos + "\r\n")
            archivo.write("Fecha de nacimiento: "+ citas.fecha_nacimiento + "\r\n")
            archivo.write("Edad: "+ citas.edad + "\r\n")
            archivo.write("Sexo: "+ citas.sexo + "\r\n")
            
            #Mostrar mensaje de exito
            print("\r\n Cita editado correctamente \r\n")
    else:
        print("Esta cita no existe")
    
    app()

def buscar_cita():
    cedula= input("Seleccione la cita que desea buscar: \r\n")
    
    try:
        with open(CARPETA+cedula+EXTENSION) as cita:
            print("\r\nInformación del Contacto: \r\n")
            for linea in cita:
                print(linea.lstrip())
    
    except IOError:
        print("El archivo no existe")
        print(IOError)
    
    app()



def unir_cita():
    print("Se uniran citas de forma aleatoria")
    archivos = os.listdir(CARPETA)
    
    archivos_txt=[i for i in archivos if i.endswith(EXTENSION)]
    
    for archivo in archivos_txt:
        with open(CARPETA+archivo) as citas:
            #Imprime los contactos en linea
            for linea in citas:
                print(linea.lstrip())
    
     
    app()    
    
def mostrar_cita():
    archivos = os.listdir(CARPETA)
    
    archivos_txt= [i for i in archivos if i.endswith(EXTENSION)]
    
    for archivo in archivos_txt:
        with open(CARPETA+archivo) as citas:
            #Imprime los contactos en linea
            for linea in citas:
                print(linea.lstrip())
    
    app()

def eliminar_cita():
    cedula= input("Seleccione la cédula que desea eliminar: \r\n")
    
    try:
        os.remove(CARPETA+cedula+EXTENSION)
        print("Contacto eliminado correctamente")
    
    except:
        print("No existe ese contacto")
    
    app()


    
            
            
            
def mostrar_menu():
    print("Seleccione una opción dentro del Menú que desee elegir")
    print("1) Agregar una cita")
    print("2) Editar una cita")
    print("3) Buscar una cita")
    print("4) Unir citas")
    print("5) Mostrar todas las citas")
    print("6) Eliminar cita")
    print("7) Salir")

def crear_directorio():
    if not os.path.exists(CARPETA):
        #Crear carpeta
        os.makedirs(CARPETA)

def existe_citas(cedula):
    return os.path.isfile(CARPETA + cedula + EXTENSION)

app()                