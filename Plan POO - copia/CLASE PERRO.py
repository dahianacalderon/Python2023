


class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def emitirLadrido(self):
        return "¡Guau! ¡Guau!"

# Crear objetos de la clase Perro
perro1 = Perro(nombre="Buddy", raza="Labrador", edad=3)
perro2 = Perro(nombre="Max", raza="Bulldog", edad=5)

# Acceder a los atributos y llamar al método
print(f"{perro1.nombre} ({perro1.raza}), Ladrido: {perro1.emitirLadrido()}")
print(f"{perro2.nombre} ({perro2.raza}), Ladrido: {perro2.emitirLadrido()}")



