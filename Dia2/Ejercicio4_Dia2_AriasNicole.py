#############
## Clase 2 ##
#############

# Algoritmo para verificar si un número es primo

# Entrada del número por consola
numero = int (input ("Ingresa un número: "))
# Definir el tipo de dato en las otras variables
x = int
num1 = int

# Condicionar el tipo de dato limitado a los naturales
if (numero < 0):
    # Salida por consola
    print("No es posible realizar la determinación")
elif (numero > 0):
    # Inicializar las variables a usar en el ciclo
    x = 0
    num1 = 0
    # Ciclo Para
    for i in range (0,i=numero,1):
        # Incremementar el valor de x en cada repetici{on}
        num1 = num1 + 1
        # Condición a cumplir para aumentar conscutivamente los divisores
        if (numero % num1 = 0):
            x = x + 1
        else (numero % num1 != 0):
            x = x
    
# Condición de cumplimiento en el resultado del ciclo
if (x = 2):
    print (numero, "Es número primo")
elif (x = 1):
    print (numero, "No es un número primo")
else:

# Desarrollado por : Nicole Dayana Arias Pinzón , identificada con número C.C. 1097496027