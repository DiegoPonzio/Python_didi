from calculo import calcul

class res(calcul):
    def ans(self):
        x = int(input("Ingresa tu primer numero: "))
        y = int(input("Ingresa tu segundo numero: "))

        if x > y:
            print("El resultado de", x, " menos ", y, " es igual a:", x-y)
        else:
            print("El resultado de", y, " menos ", x, " es igual a:", y-x)