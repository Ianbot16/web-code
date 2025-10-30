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
usuarios={}
lista=[]
citas=[]

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
            cedula=input("Ingrese el número de usuario a eliminar: \r\n")
            eliminar_usuario(cedula)
        elif opcion == 7:
            print("Saliendo del sistema, gracias por entrar.")
            exit()
        else:
            print("Incorrecto, ingrese otro número") 
        
def registrar_usuario():
    global usuarios
    global lista
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
    
    sexo=input("Ingrese su sexo (M (Masculino) o F (Femenino)): \r\n")
    while not sexo:
        print("Debe ingresar su sexo")
        sexo=registrar_usuario()
        continue
    
    fecha_nacimiento=input("Ingrese su fecha de nacimiento (YYYY-MM-DD): \r\n")
    while not fecha_nacimiento or not fecha_nacimiento.count("-") == 2:
        print("El formato de fecha ingresado no es válido. Debe ser YYYY-MM-DD.")
        fecha_nacimiento = input("Agrega Fecha de Nacimiento del Usuario (YYYY-MM-DD): \n")         
    fecha_nacimiento=datetime.datetime.strptime(fecha_nacimiento, '%Y-%m-%d')   
    edad=datetime.datetime.now().year - fecha_nacimiento.year
    fecha_nacimiento = fecha_nacimiento.strftime('%Y-%m-%d')
    print("Su edad es:\r\n",edad)
    if edad < 18:
        print("No puede ingresar es menor de edad.")
        menu()
    else:
        print("Sí puede ingresar.")
    usuarios[cedula]=nombres,apellidos,sexo,fecha_nacimiento,edad
    if usuarios not in lista:
        lista.append(usuarios)
    print(lista)
    print("Cita guardada con exito")
    menu()
    
def editar_usuario():
    global usuarios
    global lista
    print("Editar usuario")
    cedula = input("Ingrese la cedula del usuario: \r\n")
    for user in usuarios:
        if user == cedula:
            nombres=input("Ingrese sus nuevos nombres: \r\n")
            while not nombres:
                print("Debe poner sus nombres")
                nombres=editar_usuario()
                continue
            
            apellidos=input("Ingrese sus nuevos apellidos: \r\n")
            while not apellidos:
                print("Debe poner sus apellidos")
                apellidos=editar_usuario()
                continue
            
            sexo=input("Ingrese su sexo (M (Masculino) o F(Femenino)): \r\n")
            while not sexo:
                print("Debe ingresar su sexo")
                sexo=editar_usuario()
                continue
            fecha_nacimiento=input("Ingrese su fecha de nacimiento (YYYY-MM-DD): \r\n")
            while not fecha_nacimiento:
                print("Debe poner su fecha de nacimiento")
                fecha_nacimiento=editar_usuario()
                continue
            fecha_nacimiento=datetime.datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
            edad=datetime.datetime.now().year - fecha_nacimiento.year
            fecha_nacimiento = fecha_nacimiento.strftime('%Y-%m-%d')
            print("Su edad es:\r\n",edad)
            if edad < 18:
                print("No puede ingresar es menor de edad.")
                menu()
            else:
                print("Sí puede ingresar.")
            usuarios[cedula]=nombres,apellidos,sexo,fecha_nacimiento,edad
            if usuarios not in lista:
                lista.append(usuarios)
                   
        else:
            print("Esa cedula no se encuentra")
            menu()
            

def buscar_usuario():
    global usuarios
    print("Buscar cita registradas")
    cedula = input("Ingresé la cedula de la cita: \r\n")
    for user in usuarios:
        if user == cedula:
            print("""
              Cedula: {} 
              Nombres: {} 
              Apellidos: {} 
              Sexo: {} 
              Fecha de nacimiento:{}
              Edad:{} 
              """.format(user,usuarios[user][0],usuarios[user][1],usuarios[user][2],
                         usuarios[user][3],usuarios[user][4]))
        else:
            print("Esa cedula no se encuentra")

def mostrar_usuario():
    global usuarios
    print("Muestra todas las citas registradas")
    for user in usuarios:
        print("""
              Cedula: {} 
              Nombres: {} 
              Apellidos: {} 
              Sexo: {} 
              Fecha de nacimiento:{}
              Edad:{} 
              """.format(user,usuarios[user][0],usuarios[user][1],usuarios[user][2],
                         usuarios[user][3],usuarios[user][4]))
       
def unir_cita():
    global usuarios
    print("Unir citas de forma aleatoria")
    
    primera_persona=random.choice(list(usuarios.items()))
    print(primera_persona)
    
    segunda_persona=random.choice(list(usuarios.items()))
    print(segunda_persona)
    
    for datos in usuarios.items():
        print("Uniendo citas")
        if primera_persona[datos] == segunda_persona[datos]:
            print("No pueden estar juntos")
        else:
            print("Sí pueden estar juntos")
            
    
        
    
    
    
    
        
            
            
        
            
        
def eliminar_usuario(cedula):
    global usuarios
    del(usuarios[cedula])
    print("Registro borrado con exito")
    




menu()