from .funcionesGGDD import *

while True ():
    print("--------------------------------")
    print("----- Aristas -----")
    print("--------------------------------")

    #CRUD (CREATE , READ , UPDATE & DELETE)
    print("0. Cerrar programa")
    print("1. Crear artista")
    print("2. Mostrar todos los artistas")
    print("3. Mostrar un artista")
    print("4. Actualizar a un artista en específico")
    print("5. Eliminar a un artista en específico")
    
    # Entrada de la opción por consola
    opcionUsuario=int(input("Escoja una opción (Numérica):"))
    # Establecer condición
    if(opcionUsuario==1):
        # Salida por consola
        print("-------------------------")
        print("----- Crear Artista -----")
        print("-------------------------")
        numPersonas = int (input ("¿Cuántas personas deseas crear en la librería?: "))
        #Iniciar Diccionario
        infoPersona3 = {}
        # Entrada de datos por consola
        nombreUsuario = input("Ingrese el nombre de la persona: ")
        apellidoUsuario = input("Ingrese el apellido de la persona: ")
        edad = int(input("Ingrese la edad de la persona: "))
        numTelefonos = int(input("Cuántos números de teléfono tienes: "))
    