#Revisar si una condicion es mayor a
balance=0.00
if balance > 0.00:
    print("Puedes pagar")
else:
    print("No tienes saldo")
    

#Likes
likes=2000
if likes>=2000:
    print("Felicidades, 2000 likes")
else:
    print("Casi, llegaste a los 2000 likes")
    
#If con texto
lenguaje="Python"
if not lenguaje == "Python":
    print("Excelente desición")
else:
    print("Mala desición")
    
#Evaluar un booleano
usuario_autenticado=True
usuario_admin=True
if usuario_autenticado:
    if usuario_autenticado:
        print("Acceso total")
    else:
        print("Acceso al sistema.")
else:
    print("Debes iniciar sesión.")

#Evaluar un elemento de la lista
lenguajes = ["Python","C++","PHP","Java","JavaScript","C#","Kotlin"]
if "PHP" in lenguajes:
    print("PHP está disponible")
else:
    print ("PHP no está disponible")