import random
import datetime
class App_citas:
    def __init__(self,cedula,nombres,apellidos,sexo,fecha_nacimiento,edad):
        self.cedula=cedula
        self.nombres=nombres
        self.apellidos=apellidos
        self.sexo=sexo
        self.fecha_nacimiento=fecha_nacimiento
        self.edad=edad

i=0    
lista=[]
usuario={
    "cedula":" ",
    "nombres":" ",
    "apellidos":" ",
    "sexo":" ",
    "fecha de naciminto":" ",
    "edad": 0}

def menu():
    while i == 0:
        print("Menú de aplicación de citas")
        print("1) Registro de usuarios")
        print("2) Actualizar usuarios")
        print("3) Buscar usuarios")
        print("4) Mostrar usuarios registrados")
        print("5) Unir usuarios en citas")
        print("6) Eliminar un usuario")
        print("7) Salir del sistema")
        print("No presione Enter, si no ha ingresado un número")
        opcion=int(input("Seleccione una opción: \r\n"))
        if opcion == 1:
            registrar_usuario()
        elif opcion == 2:
            editar_usuario()
        elif opcion == 3:
            buscar_usuario()
        elif opcion == 4:
            mostrar_usuario()
        elif opcion == 5:
            unir_cita()
        elif opcion == 6:
            eliminar_usuario()
        elif opcion == 7:
            print("Saliendo del sistema, gracias por entrar.")
            exit()
        else:
            print("Incorrecto, ingrese otro número") 
        
def registrar_usuario():
    print("Registrar un usuario")
    cedula = input("Ingrese un número de cedula: \r\n")
    while not cedula:
        print("Debe ingresar un número de cedula")
        cedula=registrar_usuario()
        continue
        
    
    nombres = input("Ingrese sus nombres: \r\n")
    while not nombres:
        print("Debe ingresar un nombre")
        nombres=registrar_usuario
        continue
    
    apellidos = input("Ingrese sus apellidos: \r\n")
    while not apellidos:
        print("Debe ingresar un apellido")
        apellidos=registrar_usuario()
        continue
    
    sexo=input("Ingrese su sexo (M(Masculino) o F(Femenino)): \r\n")
    while not sexo:
        print("Debe ingresar su sexo")
        sexo=registrar_usuario()
        continue
    
    fecha_nacimiento=input("Ingrese su fecha de nacimiento (YYYY-MM-DD): \r\n")
    while not fecha_nacimiento:
        print("Debe poner su fecha de nacimiento")
        fecha_nacimiento=registrar_usuario()
        continue  
    fecha_nacimiento=datetime.datetime.strptime(fecha_nacimiento, '%Y-%m-%d')   
    edad=datetime.datetime.now().year - fecha_nacimiento.year
    fecha_nacimiento = fecha_nacimiento.strftime('%Y-%m-%d')
    print("Su edad es: \r\n", edad)
    if edad < 18:
        print("No puede ingresar es menor de edad.")
    else:
        print("Sí puede ingresar.")
    cita=App_citas(cedula,nombres,apellidos,sexo,fecha_nacimiento,edad)
    #usuario[cedula]= nombres,apellidos,sexo,fecha_nacimiento,edad
    lista.append(cita)
    print("Cita guardada con exito")
    
def editar_usuario():
    print("Editar usuario")
    cedula = input("Ingrese la cedula del usuario: \r\n")
    for cita in lista:
        if cita.cedula == cedula:
            cita.nombres=input("Ingrese sus nuevos nombres: \r\n")
            while not cita.nombres:
                print("Debe poner sus nombres")
                cita.nombres=editar_usuario()
                continue
            
            cita.apellidos=input("Ingrese sus nuevos apellidos: \r\n")
            while not cita.apellidos:
                print("Debe poner sus apellidos")
                cita.apellidos=editar_usuario()
                continue
            
            cita.sexo=input("Ingrese su sexo (Masculino o Femenino): \r\n")
            while not cita.sexo:
                print("Debe ingresar su sexo")
                cita.sexo=editar_usuario()
                continue
            cita.fecha_nacimiento=input("Ingrese su fecha de nacimiento (YYYY-MM-DD): \r\n")
            while not cita.fecha_nacimiento:
                print("Debe poner su fecha de nacimiento")
                cita.fecha_nacimiento=editar_usuario()
                continue
            cita.fecha_nacimiento=datetime.datetime.strptime(cita.fecha_nacimiento, '%Y-%m-%d')
            cita.edad=datetime.datetime.now().year - cita.fecha_nacimiento.year
            cita.fecha_nacimiento = cita.fecha_nacimiento.strftime('%Y-%m-%d')
            print("Su edad es: \r\n", cita.edad)
            if cita.edad < 18:
                print("No puede ingresar es menor de edad.")
            else:
                print("Sí puede ingresar.")
                   
        else:
            print("Esa cedula no se encuentra")
            

def buscar_usuario():
    print("Buscar cita registradas")
    cedula = input("Ingresé la cedula de la cita: \r\n")
    for cita in lista:
        if cita.cedula == cedula:
            print("Cedula: ",cita.cedula)
            print("Nombres: ",cita.nombres)
            print("Apellidos: ",cita.apellidos)
            print("Sexo: ",cita.sexo)
            print("Fecha de nacimiento: ",cita.fecha_nacimiento)
            print("Edad: ",cita.edad)
        else:
            print("Esa cedula no se encuentra")

def mostrar_usuario():
    print("Muestra todas las citas registradas")
    k = 0
    while k < len(lista):
        print("Cedula: ",lista[k].cedula)
        print("Nombres: ",lista[k].nombres)
        print("Apellidos: ",lista[k].apellidos)
        print("Sexo: ",lista[k].sexo)
        print("Fecha de nacimiento: ",lista[k].fecha_nacimiento)
        print("Edad: ",lista[k].edad)
        print("---------------------------------")
        
        k += 1
        

def unir_cita():
    print("Unir citas de forma aleatoria")   
    primera_persona=(random.choice(lista))
    segunda_persona=(random.choice(lista))
        
    if primera_persona["sexo"] == segunda_persona["sexo"]:
        print("Ellos no pueden estar juntos")
    else:
        print("---------------------------")
        print("Ellos si pueden estar juntos")
        print("Han sido unidos")
        print(primera_persona["nombres"])
        print("y")
        print(segunda_persona["nombres"])
        print("----------------------------")
        
            
        
        
        


def eliminar_usuario():
    print("Eliminar citas")
    global citas_app
    global lista
    cedula = input("Ingresé la cedula de la cita a eliminar: \r\n")
    for lista in lista:
        if lista.cedula == cedula:
            lista.clear(lista)
            
            print(lista)
            print("Registro eliminado")




menu()