class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def obtener_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"


class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        # Llamada al constructor de la clase base
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas

    def obtener_info(self):
        # Llamada al método de la clase base y extensión
        return f"{super().obtener_info()}, Puertas: {self.num_puertas}"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        # Llamada al constructor de la clase base
        super().__init__(marca, modelo)
        self.tipo = tipo

    def obtener_info(self):
        # Llamada al método de la clase base y extensión
        return f"{super().obtener_info()}, Tipo: {self.tipo}"


# Crear instancias de las clases
mi_coche = Coche(marca="Toyota", modelo="Corolla", num_puertas=4)
mi_moto = Moto(marca="Honda", modelo="CBR500R", tipo="Deportiva")

# Acceder a los atributos y llamar a los métodos
print(mi_coche.obtener_info())  # Salida: Marca: Toyota, Modelo: Corolla, Puertas: 4
print(mi_moto.obtener_info())   # Salida: Marca: Honda, Modelo: CBR500R, Tipo: Deportiva


