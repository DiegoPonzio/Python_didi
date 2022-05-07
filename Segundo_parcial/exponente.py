from calculo import calcul

class expo(calcul):
    def ans(self):
        x = int(input("Ingresa la base del exponente: "))
        y = float(input("Ingresa el exponente: "))
        res = pow(x,y)
        print("El resultado de la base ", x, " y el exponente", y, "es igual a:", res)