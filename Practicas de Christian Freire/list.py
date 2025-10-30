#Lista de lenguajes de programación
lenguajes = ["Python","C++","PHP","Java","JavaScript","C#","Kotlin"]
print(lenguajes)
print(lenguajes[0])

#Ordenar elementos
lenguajes.sort()
print (lenguajes)

#Accediendo a un elemento de la lista
aprendiendo=f"Estoy aprendiendo {lenguajes[6]}"
print(aprendiendo)

#Modificando elementos
lenguajes[2]="Ruby"
print(lenguajes)

#Agregando elementos
lenguajes.append("Java")
print(lenguajes)

#Eliminando elementos
del lenguajes[0]
print(lenguajes)

#Eliminando el ultimo elemento
lenguajes.pop()
print(lenguajes)

#Elimnando el elemnto seleccionado mediante metodo pop
lenguajes.pop(0)
print(lenguajes)

#Eliminar por nombre
lenguajes.remove("PHP")
print(lenguajes)



