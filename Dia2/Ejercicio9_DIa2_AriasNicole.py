#############
## Clase 2 ##
#############

# Algoritmo para generar una tabla de multipĺicar

# Entrada por consola
numero = int (input ("Ingresa un número: "))


# Condicionar el tipo de dato limitado a los naturales
if (numero >= 1):
    for i in range (1,11,1):
        numero * i
        # Salida por consola
        print(f"{numero} × {i} = {numero * i}")
