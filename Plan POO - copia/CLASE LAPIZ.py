class Lapiz:

    def __init__(self, color, contiene_borrador, usa_grafito):
        self.color = color
        self.contiene_borrador = contiene_borrador
        self.usa_grafito = usa_grafito

    def dibujar(self):
        print("El lapiz esta dibujando.")

    def borrar(self):
        if self.contiene_borrador:
            print("El lapiz esta borrando.")
        else:
            print("No es posible borrar.")

    def es_valido_para_borrar(self):
        return self.contiene_borrador


lapiz_generico = Lapiz("azul", True, False)
lapiz_generico.dibujar()
lapiz_generico.contiene_borrador = True
lapiz_generico.borrar()


