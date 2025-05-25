#############
## Clase 2 ##
#############

# Ejercicio de Ciclos CostumeRappid

numHamb = int (input ("Bienvenido a Custom Rapidd! ¿Cuántas hamburguesas deseas ordenar?: "))

# 
if (numHamb >= 1):
    print("Personaliza tu pedido con el siguiente menú de opciones: ")
    for i in range (0, numHamb):
        costoPedido = 0
        pan = int( input ("Ingresa el tipo de pan deseado \n. (1) Pan de Centeno por $1000= | (2) Pan de Avena por $1500= "))
        if (pan == 1):
            costoPedido = 0 + 1000
            print (costoPedido)
        elif (pan == 2):
            costoPedido = 0 + 1500
            print (costoPedido)
        else:
            print ("Por favor, selecciona opción 1 o 2")
        
        carne = int( input ("Ingresa la cantidad de Carne deseada \n. (1) Carne de 250g por $5000= |(2) Carne de 350g por $7000= "))
        if (carne == 1):
            costoPedido = costoPedido + 5000
            print (costoPedido)
        elif (carne == 2):
            costoPedido = costoPedido + 7000
            print (costoPedido)
        else:
            print ("Por favor, selecciona opción 1 o 2")
        
        pollo = int( input ("Ingresa la cantidad de Pollo deseado \n. (1) Pollo de 250g por $4500= | (2) Pollo de 350g por $5500= "))
        if (pollo == 1):
            costoPedido = costoPedido + 4500
            print (costoPedido)
        elif (pollo == 2):
            costoPedido = costoPedido + 5500
            print (costoPedido)
        else:
            print ("Por favor, selecciona opción 1 o 2")
        
        polloDesmechado = int( input ("Ingresa la cantidad de Pollo Desmechado deseado \n. (1) Pollo Desmechado de 250g por 6500= | (2) Pollo Desmechado de 350g por $7500= "))
        if (polloDesmechado == 1):
            costoPedido = costoPedido + 6500
            print (costoPedido)
        elif (polloDesmechado == 2):
            costoPedido = costoPedido + 7500
            print (costoPedido)
        else:
            print ("Por favor, selecciona opción 1 o 2")
        
        tocineta = int( input ("Ingresa la cantidad de Tocineta deseada \n. (1) Lonja por $1500= | (2) Lonjas por $2500= "))
        if (tocineta == 1):
            costoPedido = costoPedido + 1500
            print (costoPedido)
        elif (tocineta == 2):
            costoPedido = costoPedido + 2500
            print (costoPedido)
        else:
            print ("Por favor, selecciona opción 1 o 2")
        
        papasFritas = int( input ("Ingresa el tipo Papas Fritas deseadas \n. (1) A la francesa por $5000= | (2) En Cascos por $6000= "))
        if (papasFritas == 1):
            costoPedido = costoPedido + 5000
            print (costoPedido)
        elif (papasFritas == 2):
            costoPedido = costoPedido + 6000
            print (costoPedido)
        else:
            print ("Por favor, selecciona opción 1 o 2")

        Bebida = int( input ("Ingresa tu Bebida deseada \n. (1) Gaseosa por $5000= | (2) Cerveza Club Colombia por $8000= | (3) Naranjada por $9000="))
        if (Bebida == 1):
            costoPedido = costoPedido + 5000
            print (costoPedido)
        elif (Bebida == 2):
            costoPedido = costoPedido + 8000
            print (costoPedido)
        elif (Bebida == 3):
            costoPedido = costoPedido + 9000
            print (costoPedido)
        else:
            print ("Por favor, selecciona opción 1, 2 o 3")
else:
    print ("Se necesita un valor contable")

servicio = float(0.1)
total = costoPedido + (costoPedido * servicio)

print ("Servicio prestado al cliente : (10%) \n.  El valor total a ser cancelado es : $" total " COP ")