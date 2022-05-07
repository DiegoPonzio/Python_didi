entrada = int(input("Ingrese la edad de la persona que ingresara al juego: "))

if entrada <= 10:
    entrada = entrada-entrada*0.25

print("El costo de la entrada seria de: $", entrada)
