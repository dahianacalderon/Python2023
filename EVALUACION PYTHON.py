# REGISTRO DEL VOTANTE
# INGRESO AL SISTEMA DE VOOTACION CON EL ID DEL VOTANTE
# VOTAR POR UN CANDIDATO(SOLO UNA VEZ) ADEMAS SE DEBE CONSIDERAR EL VOTO EN BLANCO


registro={}
candidatos= ["julio","juan","armando","blanco"]
votante={}
id=()

# Buscar un dato en la lista (nombre )
entrada = input("Deseas buscar por nombre [si]")
                
def votarPorUnCandidato():

 if entrada.lower() == "si":
    buscar = input("Ingresa el nombre del candidato: ")
    if buscar in candidatos:
        indice = candidatos.index(buscar)
        print("votaste por el canditato {buscar}")
    else:
        print("La persona que buscas no esta en la lista.")  


# Listas
nombres = ['julio', 'juan', 'armando','blanco'] 

# Función para agregar el registro del votante
def agregarRegistro():
    id = input("Ingrese el ID: ")
    nombre = input("Ingrese el nombre: ")
    nacionalidad = input("Ingrese su nacinalidad: ")
    registro [id] = {"ID": id, "nombre": nombre, "nacionalidad":nacionalidad }
    print("Su registro se ha agregado con exito.")



#ingreso al sistema de votacion con el id del votante
def ingresarConId():
    id= int(input("ingrese el id del votante"))
    print("haz ingresado con exito al sistema de votacion ")

while True:
    print("\nOpciones:")
    print("1. agregar registro")
    print("2. ingresar con id")
    print("3. votar por un candidato")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregarRegistro()
    elif opcion == "2":
        ingresarConId()
    elif opcion == "3":
        votarPorUnCandidato()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
        



    
    


