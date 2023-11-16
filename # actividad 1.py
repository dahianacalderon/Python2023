# Un diccionario para almacenar la información de los equipos.
equipos = {}

# Una lista para almacenar novedades.
novedades = []

# Función para agregar un equipo con su ID, cargador y mouse.
def agregar_equipo():
    id_equipo = input("Ingrese el ID del equipo: ")
    cargador = input("Ingrese el nombre del cargador: ")
    mouse = input("Ingrese el nombre del mouse: ")
    equipos[id_equipo] = {"ID": id_equipo, "Cargador": cargador, "Mouse": mouse}
    print("Equipo agregado con éxito.")

# Función para agregar una novedad sobre un equipo.
def agregar_novedad():
    id_equipo = input("Ingrese el ID del equipo relacionado a la novedad: ")
    fecha = input("Ingrese la fecha de la novedad: ")
    descripcion = input("Ingrese la descripción de la novedad: ")
    novedades.append({"ID": id_equipo, "Fecha": fecha, "Descripción": descripcion})
    print("Novedad agregada con éxito.")

# Función para mostrar un reporte de equipos con novedades.
def mostrar_reporte_novedades():
    for novedad in novedades:
        equipo = equipos.get(novedad["ID"])
        if equipo:
            print(f"Equipo ID: {equipo['ID']}, Cargador: {equipo['Cargador']}, Mouse: {equipo['Mouse']}")
            print(f"Fecha de la novedad: {novedad['Fecha']}")
            print(f"Descripción: {novedad['Descripción']}\n")

# Ejemplo de uso de las funciones:
while True:
    print("\nOpciones:")
    print("1. Agregar equipo")
    print("2. Agregar novedad")
    print("3. Mostrar reporte de novedades")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_equipo()
    elif opcion == "2":
        agregar_novedad()
    elif opcion == "3":
        print("Reporte de Equipos con Novedades:")
        mostrar_reporte_novedades()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

