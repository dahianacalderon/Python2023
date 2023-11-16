import random

aprendices = ["Juan Diego", "Mathew Guarnizo", "Maria Fernanda", "Melissa", "Nicolas Paulo", "Miguel Angel", "Stiven", "Maicol Esteban", "Kevin Londono", "Marlon", "Maria Jose", "Nataly", "Camila", "Stiwar"]
edades = []

#pedir la edad por tecla 
for aprendiz in aprendices:
    edad = int(input(f"ingrese la edad de {aprendiz}: "))
    edades.append(edad)

print(aprendices)
print(edades)

instructora = input("ingrese el nombre de la instructora")
aprendices.insert(0, instructora)
print(aprendices)


# Eliminar a Adriana Lucia de la lista
eliminar = input('Deseas eliminar a la instructora "Adriana Lucia" de la lista [si o no]: ')
if instructora in aprendices:
    aprendices.remove(instructora)
    print(f"Se eliminó a {instructora} de la lista de aprendices.")
else:
    print(f"{instructora} no se encontró en la lista de aprendices.")

print(aprendices)

# Buscar un dato en la lista (nombre o edad)
entrada = input("Deseas buscar por nombre [n] o por edades [e]: ")

if entrada.lower() == "n":
    buscar = input("Ingresa el nombre del aprendiz que deseas buscar: ")
    if buscar in aprendices:
        indice = aprendices.index(buscar)
        edad = edades[indice]
        print(f"El aprendiz {buscar} tiene {edad} anos de edad.")
    else:
        print("La persona que buscas no esta en la lista.")
elif entrada.lower() == "e":
    buscar = int(input("Ingresa la edad del aprendiz que deseas buscar: "))
    if buscar in edades:
        indice = edades.index(buscar)
        nombre = aprendices[indice]
        print(f"El aprendiz que tiene {buscar} anos de edad se llama {nombre}.")
    else:
        print("La persona que buscas no esta en la lista.")
else:
    print("Opcion no valida. Por favor, selecciona 'n' o 'e'.")

# Mostrar rango de aprendices
mostrar = input("Deseas ver un rango de aprendices (10 primeros, 10 ultimos) [si o no]: ")

if mostrar.lower() == "si":
    rango = input("Que rango deseas ver (10 primeros [p] o 10 ultimos [u]): ")
    if rango.lower() == "p":
        print(aprendices[:10])
        print(edades[:10])
    elif rango.lower() == "u":
        print(aprendices[-10:])
        print(edades[-10:])
    else:
        print("Opcion no valida. Por favor, selecciona 'p' o 'u'.")
else:
    print(aprendices)
    print(edades)
