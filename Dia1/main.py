###############
# Clase dia 1 #
###############

# Creado por : Nicole Dayana Arias Pinzón                       # T.I: 1097496027

# Imprimir en piton
print("hola mundo!")
# Creación de variables
# 1. Dato tipo string
nombre = "Nicole"
print(type(nombre))
# 2. Dato tipo numero entero
numeroEntero = 5
print (numeroEntero)
print (type(numeroEntero))
# 3. Dato tipo numero real
numeroReal = 5.3
print (type(numeroReal))
# 4. Dato tipo double
numeroPi = 3.1416
print (numeroPi)
# 5. Dato tipo booleano
booleanito = True
print (booleanito)
# 6. (SOLO PYTHON) Numero complejo
numeroComplejo = complex ('+1.23')
print (numeroComplejo)
print(type(numeroComplejo))
# Convertir numero int a float
numeroNuevo = (float(numeroEntero))
print (numeroNuevo)
print (" ")
# Ciclo for (Desde)
for i in range (5):
    print (i)
print (" ")
# (Desde - Hasta)
for i in range (0,5):
    print (i)
print (" ")
for i in range (1,5):
    print (i)
print (" ")
# (Desde - Hasta - Paso)
for i in range (1,5,1):
    print (i)
print (" ")
# #####################
# Ciclo while
booleanitoNuevo = True
while (booleanitoNuevo == True):
    print ("Sigo siendo verdadero")
    booleanitoNuevo == False

while (booleanitoNuevo == True):
    print ("Sigo siendo verdadero")
    booleanitoNuevo == False

print (" ")
# #################################
# Condicionales if - else
texto = "Nicole"
if (texto == "Corpus"):
    print("Sos Corpus")
else:
    if (texto == "Sharick")
        print ("Sos Sharick")
    else:
        print ("No sos Ninguno")

#Condicionales elif
if (texto == "Corpus"):
    print("Sos Corpus")
elif(texto == "Sharick"):
    print ("Sos Sharick")
else:
    print ("No sos Ninguno")

# ##########################
# Anidar condicionales
booleanitoCorpus1 = True
booleanitoCorpus2 = False
if (booleanitoCorpus1 == True and booleanitoCorpus2 == True):
    print("Todos somos verdaderos")
else: 
    print("No somos iguales")
 # ##########################
 # Entradas de Usuario
nombreUsuario = input ("Cuál es tu nombre") #Todos los inputs son string
print ("Tu nombre es :" + nombreUsuario) # Concatenación
# Casteo de string a numero
edadUsuario = int(input("¿Cuál es tu edad"))
edadUsuario = edadUsuario + 5
print ("La edade de "+nombreUsuario+" es de :" + str(edadUsuario))

# ################################################################
# Funciones 
# 1. Funcion con retorno y con parámetros
def areaCirculo (radio):
    valorPi = 3.1416
    resultadoFinal = valorPi * (radio**2)
    return resultadoFinal
radioUsuario = float(input("¿Cuál es el radio de su círculo?"))
print ("El área del círculo es de:" +str(int(areaCirculo(radioUsuario))))
# 2. Funcion con retorno y sin parámetros
def valorDolar():
    return 4299
valorFinalDolar = valorDolar
print("El valor del dólar es : "+ str(valorFinalDolar))
# 3. Función sin retorno y con parámetros
def concatenarNombres (nombre,apellido):
    print("Su nombre completo es: "+nombre+" "+apellido+"")
concatenarNombres("Sharick", "Ibañez")
# 4. Función sin retorno y sin parámetros
def funcionX():
    print("Soy una función que vive y existe")
funcionX()

# Desarrollado por : Nicole Dayana Arias Pinzón #