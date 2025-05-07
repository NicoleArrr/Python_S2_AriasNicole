#############
## Clase 2 ##
#############

# Algoritmo para encontrar el mayor de tres números

# Entrada de ls números por consola
num1 = int ( input ("Ingresa un número: "))
num2 = int ( input ("Ingresa un número: "))
num3 = int ( input ("Ingresa un número: "))

# Realizar comparaciones entre ellos haciendo uso de condicionales
if (num1 >= num2) or (num1 >= num3):
    # Salida por consola si se cumple la condición descrita
    print (num1, " Es el mayor de los tres números")
elif (num2 >= num3):
    # Salida por consola si se cumple la condición descrita
    print (num2, " Es el mayor de los tres números")
else:
    # Salida por consola si se cumple la condición descrita
    print (num3, " Es el mayor de los tres números")

# Desarrollado por : Nicole Dayana Arias Pinzón , identificada con número C.C. 1097496027