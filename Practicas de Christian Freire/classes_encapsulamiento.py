class Restaurant:
    def __init__(self,nombre,categoria,precio):
        self.nombre=nombre #Atributo
        self.categoria=categoria
        self.__precio=precio #Default: publicas,protected,private

    def mostrar_informacion(self):
        print(f"Nombre de restaurante: {self.nombre}, Categoría: {self.categoria}, Precio: {self.__precio}")
        
    #Getters y Setters -GET: obtiene un valor y SET: Agrega un valor o lo modifica
    def get_precio(self):
        return self.__precio
        
    def set_precio(self,precio):
        self.__precio=precio
        
#Instanciar una clase
restaurant=Restaurant("Pizzeria Italiano","Comida italiana",5)

#restaurant.__precio=10 #No va a ser posible modificarlo de esta manera con private __variable
restaurant.mostrar_informacion()
restaurant.set_precio(10)
precio=restaurant.get_precio()
print(precio)

#Segunda instancia
restaurant2=Restaurant("Hamburguesas Python","Comida Rápida",3)

#restaurant2.__precio=6
restaurant2.mostrar_informacion()
restaurant2.set_precio(6)
precio=restaurant2.get_precio()
print(precio)
