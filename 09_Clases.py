class Animal:
    def __init__(self,nombre):
        self.nombre=nombre

    def __comer__(self):
        pass

class Conejo(Animal):
    def comer(self):
        return f"{self.nombre} come alfalfa"

class Perro(Animal):
    def comer(self):
        return f"{self.nombre} come carne"

paco_conejo=Conejo("Paco")
luna_perro=Perro("Luna")

print(paco_conejo.comer())
print(luna_perro.comer())