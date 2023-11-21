class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def obtenerInfo(self):
        return f"{self.titulo}, escrito por {self.autor}, {self.paginas} páginas."

# Se están creando objetos en la clase Libro
libro1 = Libro(titulo="Python para Principiantes", autor="John Smith", paginas=200)
libro2 = Libro(titulo="Introducción a la Programación", autor="Alice Johnson", paginas=150)

# Se accede a los atributos y se llama al método
print(libro1.obtenerInfo())
print(libro2.obtenerInfo())
