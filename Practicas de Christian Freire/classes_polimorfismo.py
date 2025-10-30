class Restaurant:
    def __init__(self,nombre,categoria,precio):
        self.nombre=nombre #Atributo
        self.categoria=categoria
        self.precio=precio #Default: publicas,protected,private

    def mostrar_informacion(self):
        print(f"Nombre de restaurante: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}")
        
    #Getters y Setters -GET: obtiene un valor y SET: Agrega un valor o lo modifica
    def get_precio(self):
        return self.precio
        
    def set_precio(self,precio):
        self.precio=precio


#Crear una clase hijo de la clase restaurante
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, alberca):
        super().__init__(nombre, categoria, precio)
        self.alberca = alberca
        
    #Reescribir un metodo (debe llamarse igual)
    def mostrar_informacion(self):
        print(f"Nombre de restaurante: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}, Alberca: {self.alberca}")    
        
    #Agregar un metodo que solo exista en la clase Hotel
    def get_alberca(self):
        return self.alberca
    
    
        
hotel = Hotel("Hotel Python","5 Estrellas",200,"Si")
hotel.mostrar_informacion()
alberca=hotel.get_alberca()
print(alberca)
