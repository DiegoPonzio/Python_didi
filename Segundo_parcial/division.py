from calculo import calcul

class div(calcul):
    def ans(self):
        x = int(input("Ingresa el dividendo de su fraccion: "))
        y = int(input("Ingrese el divisor de su fraccion: "))
        res = int(x/y)
        print("El resultado de la división de ", x, " entre ", y, " es: ", res)
        print("Y su residuo es: ", (x % y))