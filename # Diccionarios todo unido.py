# Diccionarios
calificaciones = {
    'Sandra': 5.0,
    'Adriana': 5.0,
    'Mauricio': 4.5,
    'Jose': 2.5
}

for nombre, nota in calificaciones.items():
    print(nombre, nota)

# Técnicas de iteración de diccionarios
print("Técnicas por clave")
for nombre in calificaciones.keys():
    print(nombre)

print("Iterar por valor")
for nota in calificaciones.values():
    print(nota)

# Listas
nombres = ['Maria', 'Sebastian', 'Ana']
edades = ['18', '25', '30']

for nombre, edad in zip(nombres, edades):
    print(f'Tu nombre es {nombre} y tu edad {edad}.')

# Operaciones sobre los diccionarios
dicaleatorio = {x: x**2 for x in (2, 4, 6)}
print(dicaleatorio)

# Imprimir números en reversa
print("Números en reversa")
for i in reversed(range(1, 10, 2)):
    print(i)

# Borrar un elemento del diccionario
if 'Rosa' in calificaciones:
    del calificaciones['Rosa']

for nombre, nota in calificaciones.items():
    print(nombre, nota)

# Funciones
def saludar():
    print("saludo")

def retornarnumero():
    return 1

saludar()
retornado = retornarnumero()

if retornado == 1:
    print("Devolvió un uno")
else:
    print("No devolvió un uno")

# Funciones con parámetros
def raiz(x, y):
    return x**2 + y**2

resultado = raiz(3, 5)
print(f'El resultado es: {resultado}')

def validarsiexiste(obj):
    if obj:
        print(f"{obj} is True")
    else:
        print(f"{obj} is False")

validarsiexiste(1)

# Funciones con parámetros posicionales
def compra(marca, cantidad, valor):
    return {
        'marca': marca,
        'cantidad': cantidad,
        'valor': valor * cantidad
    }

print(f'Lo comprado fue: {compra("AMD", 3, 2500000)}')

# Funciones con parámetros nominales
def compra(marca, cantidad, valor):
    return {
        'marca': marca,
        'cantidad': cantidad,
        'valor': valor * cantidad
    }

print(f'Lo comprado fue: {compra(marca="AMD", cantidad=3, valor=2500000)}')

# Parámetros por defecto
def compra(marca, cantidad, valor=2500000):
    return {
        'marca': marca,
        'cantidad': cantidad,
        'valor': valor * cantidad
    }

print(f'Lo comprado fue: {compra("AMD", 3)}')

# Modificando parámetros mutables
def lista(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

lista('domingo', [])

# Funciones anónimas (lambda)
numero_palabras = lambda t: len(t.strip().split())
print(numero_palabras("hola, esto es una prueba con lambda"))

operadorand = lambda x, y: x & y

for i in range(2):
    for j in range(2):
        print(f"{i} & {j} = {operadorand(i, j)}")
