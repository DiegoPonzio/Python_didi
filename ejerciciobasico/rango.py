valor = int(input("Ingrese un numero entre 0 y 20: "))

while valor < 0 or valor > 20:
    valor = int(input("Ingrese un numero entre 0 y 20: "))

print("El numero que tecleo es ", valor, "Se encuentra en el rango (0-20)")