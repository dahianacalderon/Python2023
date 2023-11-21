

class Persona:
    def init (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def obtenerInfo(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

# Clase derivada que hereda de Persona
class Estudiante(Persona):
    def init (self, nombre, edad, notaPromedio):
        # Llamada al constructor de la clase base
        super(). init (nombre, edad)
        self.notaPromedio = notaPromedio

    def obtenerInfo(self):
        # Llamada al método de la clase base y extensión
        return f"{super().obtenerInfo()}, Nota Promedio: {self.notaPromedio}"

# Crear objeto de la clase derivada
miEstudiante = Estudiante(nombre="Ana", edad=20, notaPromedio=8.5)

# Acceder a los atributos y llamar a los métodos
print(miEstudiante.obtenerInfo())  # Salida: Nombre: Ana, Edad: 20, Nota Promedio: 8.5






