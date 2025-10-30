class Restaurant:
    def agregar_restaurant(self,nombre):
        self.nombre=nombre #Atributo
    
    def mostrar_informacion(self):
        print(f"Nombre de restaurante: {self.nombre}")


#Instanciar una clase
restaurant=Restaurant()
restaurant.agregar_restaurant("Pizzeria Italiano")
restaurant.mostrar_informacion()

#Segunda instancia
restaurant2=Restaurant()
restaurant2.agregar_restaurant("Hamburguesas Python")
restaurant2.mostrar_informacion()

#Mostrar la información
print(f"Nombre del restaurante: {restaurant.nombre}")
print(f"Nombre del restaurante: {restaurant2.nombre}")