import random
lista=list()
usuario={
    "cedula":" ",
    "nombres":" ",
    "apellidos":" ",
    "sexo":" ",
    "fecha de Naciminto":" ",
    "edad": 0
}
import datetime
class citas_app:
    def __init__(self):
        self.cedula=(" ")
        self.nombres=(" ")
        self.apellidos=(" ")
        self.sexo=(" ")
        self.fecha_nacimiento=(" ")
        self.edad=()
    


def menu():
    opcion=0
    while opcion !=7:
        print("Menú de aplicación de citas")
        print("1) Registro de citas")
        print("2) Actualizar citas")
        print("3) Buscar citas")
        print("4) Mostrar citas registradas")
        print("5) Unir citas")
        print("6) Eliminar una cita")
        print("7) Salir")
        opcion=int(input("Seleccione una opción: \r\n"))
        if opcion == 1:
            registrar_cita()
        elif opcion == 2:
            editar_cita()
        elif opcion == 3:
            buscar_cita()
        elif opcion == 4:
            mostrar_cita()
        elif opcion == 5:
            unir_cita()
        elif opcion == 6:
            eliminar_cita()
        elif opcion == 7:
            print("Saliendo")
        else:
            print("Incorrecto, ingrese otro número") 
        
def registrar_cita():
    print("Registrar cita")
    cita=citas_app()
    cita.cedula=input("Introduce un numero de cedula: \r\n")
    cita.nombres=input("Ingrese sus nombres: \r\n")
    cita.apellidos=input("Ingrese sus apellidos: \r\n")
    cita.sexo=input("Ingrese su sexo (Masculino o Femenino): \r\n")
    cita.fecha_nacimiento=input("Ingrese su fecha de nacimiento (YYYY-MM-DD): \r\n")
    cita.fecha_nacimiento=datetime.datetime.strptime(cita.fecha_nacimiento, '%Y-%m-%d')
    cita.edad=datetime.datetime.now().year - cita.fecha_nacimiento.year
    cita.fecha_nacimiento = cita.fecha_nacimiento.strftime('%Y-%m-%d')
    print("Su edad es: \r\n", cita.edad)
    
    if cita.edad < 18:
        print("No puede ingresar es menor de edad.")
    else:
        print("Sí puede ingresar.")
        
    lista.append(cita)
    
def editar_cita():
    print("Editar cita")

def buscar_cita():
    print("Buscar cita registradas")
    busqueda = input("Ingresé la cedula de la cita: \r\n")
    for cita in lista:
        if cita.cedula == busqueda or cita.nombre == busqueda:
            print("Cedula: ",cita.cedula)
            print("Nombres: ",cita.nombres)
            print("Apellidos: ",cita.apellidos)
            print("Sexo: ",cita.sexo)
            print("Fecha de nacimiento: ",cita.fecha_nacimiento)
            print("Edad: ",cita.edad)
        else:
            print("Esa cedula no se encuentra")

def mostrar_cita():
    print("Muestra todas las citas registradas")
    for cita in lista:
        print("Cedula: ",cita.cedula)
        print("Nombres: ",cita.nombres)
        print("Apellidos: ",cita.apellidos)
        print("Sexo: ",cita.sexo)
        print("Fecha de nacimiento: ",cita.fecha_nacimiento)
        print("Edad: ",cita.edad)
        

def unir_cita():
    print("Unir citas de forma aleatoria")
    primera_cita=(random.choice(lista))
    segunda_cita=(random.choice(lista))
    
    if primera_cita == segunda_cita:
        print("Ellos no pueden estar juntos")
    else:
        print("Ellos si pueden estar juntos")
        print(primera_cita,segunda_cita)

def eliminar_cita():
    print("Eliminar citas")
    cedula = input("Ingresé la cedula de la cita a eliminar: \r\n")
    for cita in lista:
        if cita.cedula==cedula:
            cita.clear()
        else:
            print("Esa cita no se encuentra.")

def salir():
    print("Saliendo")

menu()