num = 0
valor = int(input("Ingrese un numero entre 0 y 20: "))

while valor < 0 or valor > 20:
    valor = int(input("Ingrese un numero entre 0 y 20: "))
    num += 1

print("El numero que tecleo es ", valor, "y se encuentra en el rango (0-20)")
print("El numero de veces que ingreso mal el dato fue de", num)
