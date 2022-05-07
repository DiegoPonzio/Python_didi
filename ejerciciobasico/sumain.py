n = int(input("Ingrese un numero el cual deseas sumar: "))
sum = 0

while n > 0:
    n = n+sum
    sum = int(input("Ingrese otro numero que deseas sumar de lo contrario ingrsa 0: "))
    if sum == 0:
        break

print("La suma de los numeros es: ", n)