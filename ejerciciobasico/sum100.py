n = int(input("Ingrese un numero el cual deseas sumar: "))
sum = 0

while n > 0:
    n = n+sum
    sum = int(input("Ingrese otro numero que deseas sumar si la suma es mayor a 100 el proseso se acaba"))
    if n > 100:
        break

print("La suma de los numeros es: ", n)
