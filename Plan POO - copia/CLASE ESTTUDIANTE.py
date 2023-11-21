

class Estudiante:
    def init (self, nombre, edad, notaPromedio):
        self.nombre = nombre
        self.edad = edad
        self.notaPromedio = notaPromedio

    def esAprobado(self):
        return self.notaPromedio >= 7

# Se cra objetos de la clase Estudiante
estudiante1 = Estudiante(nombre="Ana", edad=20, notaPromedio=8.5)
estudiante2 = Estudiante(nombre="Pedro", edad=22, notaPromedio=6.5)

# Accede a los atributos y llama el metodo
print(f"{estudiante1.nombre} ¿aprobado? {estudiante1.esAprobado()}")
print(f"{estudiante2.nombre} ¿aprobado? {estudiante2.esAprobado()}")



