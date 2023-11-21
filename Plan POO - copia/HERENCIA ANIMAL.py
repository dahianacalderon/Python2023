

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def obtenerInfo(self):
        return f"Nombre: {self.nombre}"

# Clase derivada que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, raza):
        # Llamada al constructor de la clase base
        super().__init__(nombre)
        self.raza = raza

    def obtenerInfo(self):
        # Llamada al método de la clase base y extensión
        return f"{super().obtenerInfo()}, Raza: {self.raza}"

# Crear objeto de la clase derivada
miPerro = Perro(nombre="Buddy", raza="Labrador")

# Acceder a los atributos y llamar a los métodos
print(miPerro.obtenerInfo())  # Salida: Nombre: Buddy, Raza: Labrador





