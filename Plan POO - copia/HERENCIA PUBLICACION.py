
class Publicacion:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def obtenerInfo(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"

# Clase que deriva la herencia de Publicacion
class Libro(Publicacion):
    def __init__(self, titulo, autor, paginas):
        # Llamada al constructor de la clase base
        super().__init__(titulo, autor)
        self.paginas = paginas

    def obtenerInfo(self):
        # Llamada al método de la clase base y extensión
        return f"{super().obtenerInfo()}, Páginas: {self.paginas}"

# Crear objeto de la clase derivada
miLibro = Libro(titulo="Python para Principiantes", autor="John Smith", paginas=200)

# Acceder a los atributos y llamar a los métodos
print(miLibro.obtenerInfo())  # Salida: Título: Python para Principiantes, Autor: John Smith, Páginas: 200

