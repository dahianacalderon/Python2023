

class Libro:
    def init (self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def obtenerInfo(self):
        return f"{self.titulo}, escrito por {self.autor}, {self.paginas} paginas."

#Se esta Creando objetos en la clase Libro
libro1 = Libro(titulo="Python para Principiantes", autor="John Smith", paginas=200)
libro2 = Libro(titulo="Introducción a la Programacion", autor="Alice Johnson", paginas=150)

# Se accede a los atributos y llama al metodo
print(libro1.obtenerInfo())
print(libro2.obtenerInfo())



