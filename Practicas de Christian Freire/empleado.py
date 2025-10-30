class Empleado:
#Ingresando los datos
    def __init__(self,nombre,apellido,salario_mensual):
        self.nombre=nombre
        self.apellido=apellido
        self.salario_mensual=salario_mensual
        
#Mostrar el nombre completo   
    def nombre_completo(self):
        print("El nombre del empleado es:", self.nombre, self.apellido)
        print("El salario es: ",self.salario_mensual)

#Mostrar el salario anual    
    def salario_anual(self):
        salario_anual=self.salario_mensual*12
        print(salario_anual)
        
#Mostrar el aumento de salario        
    def aumentar_salario(self,porcentaje):
        aumentar_salario=self.salario_mensual * porcentaje
        nuevo_salario=self.salario_mensual + aumentar_salario
        print(aumentar_salario)
        print(nuevo_salario)
    
    

#Instanciar las clases       
#Objeto 1
empleado1=Empleado("Christian","Freire",450.00)
empleado1.nombre_completo()
empleado1.salario_anual()
empleado1.aumentar_salario(0.1)
#Objeto 2
empleado2=Empleado("David","Vera",547)
empleado2.nombre_completo()
empleado2.salario_anual()



    
    

        
