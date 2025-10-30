class Restaurant:
    def __init__(self,nombre,categoria,precio):
        self.nombre=nombre #Atributo
        self.categoria=categoria
        self.precio=precio

    def mostrar_informacion(self):
        print(f"Nombre de restaurante: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}")

#Instanciar una clase
restaurant=Restaurant("Pizzeria Italiano","Comida italiana",5)
restaurant.mostrar_informacion()


#Segunda instancia
restaurant2=Restaurant("Hamburguesas Python","Comida Rápida",3)
restaurant2.mostrar_informacion()
