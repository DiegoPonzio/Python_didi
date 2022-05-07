from calculo import calcul

class sum(calcul):
    def ans(self):
        x = int(input("Ingresa un numero que dese sumar: "))
        y = int(input("Ingrese su segundo numero: "))
        print("El resultado de la suma de ", x, " mas ", y, " es igual a: ", x+y)