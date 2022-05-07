from calculo import calcul

class multi(calcul):
    def ans(self):
        x = int(input("Ingresa tu multiplicando: "))
        y = int(input("Ingresa tu multiplicador: "))
        print("El resultado de la multiplicacion de ", x, " por ", y, " es igual a: ", x*y)
