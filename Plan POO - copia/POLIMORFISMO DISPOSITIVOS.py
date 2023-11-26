class DispositivoAlmacenamiento:
    def almacenar_datos(self, datos):
        pass

class DiscoDuro(DispositivoAlmacenamiento):
    def almacenar_datos(self, datos):
        return f"Datos almacenados en el disco duro: {datos}"

class MemoriaUSB(DispositivoAlmacenamiento):
    def almacenar_datos(self, datos):
        return f"Datos almacenados en la memoria USB: {datos}"

class TarjetaSD(DispositivoAlmacenamiento):
    def almacenar_datos(self, datos):
        return f"Datos almacenados en la tarjeta SD: {datos}"

# Función que utiliza polimorfismo
def almacenar_datos_en_dispositivo(dispositivo, datos):
    print(dispositivo.almacenar_datos(datos))

# Crear instancias de las clases
mi_disco_duro = DiscoDuro()
mi_memoria_usb = MemoriaUSB()
mi_tarjeta_sd = TarjetaSD()

# Llamar a la función con diferentes tipos de dispositivos de almacenamiento
almacenar_datos_en_dispositivo(mi_disco_duro, "Información confidencial")
almacenar_datos_en_dispositivo(mi_memoria_usb, "Fotos de vacaciones")
almacenar_datos_en_dispositivo(mi_tarjeta_sd, "Documentos importantes")


