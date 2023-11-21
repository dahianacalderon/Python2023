
class Empleado:
    def calcularSalario(self):
        pass

class Asalariado(Empleado):
    def __init__(self, salario_mensual):
        self.salario_mensual = salario_mensual

    def calcularSalario(self):
        return self.salario_mensual

class PorHoras(Empleado):
    def __init__(self, horas_trabajadas, tarifa_por_hora):
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcularSalario(self):
        return self.horas_trabajadas * self.tarifa_por_hora



