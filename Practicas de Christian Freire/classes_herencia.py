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


#Crear una clase hijo de la clase restaurante
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)
        
hotel = Hotel("Hotel Python","5 Estrellas",200)
hotel.mostrar_informacion()