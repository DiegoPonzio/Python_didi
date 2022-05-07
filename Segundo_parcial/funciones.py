import math

from calculo import calcul

class function(calcul):
    def ans(self):
        bandera1 = 1
        while bandera1 == 1:
            print("----------------------------------")
            print("Funciones trigonometricas")
            print(" 1.Seno")
            print(" 2.Coseno")
            print(" 3.Tangente")
            print(" 4.Cotangente")
            print(" 5.Secante")
            print(" 6.Cosecante")
            print(" 7.Salir")
            print("-----------------------------------")
            select = int(input("Seleccione un numero: "))
            if select == 1:
                x = float(input("Ingresa el numero en grados para optener su razon trigonometrica: "))
                res = math.sin(x)
                print("El resultado del seno de ", x, " es igual a: ", res)
                select = 0
            elif select == 2:
                x = float(input("Seleccione un numero: "))
                res = math.cos(x)
                print("El resultado del coseno de ", x, " es igual a: ", res)
                select = 0
            elif select == 3:
                x = float(input("Ingresa el numero en grados para optener su razon trigonometrica: "))
                res = math.tan(x)
                print("El resultado de la tangente de ", x, " es igual a: ", res)
                select = 0
            elif select == 4:
                x = float(input("Ingresa el numero en grados para optener su razon trigonometrica: "))
                res = math.cos(x)/math.sin(x)
                print("El resultado de la cotangente de ", x, " es igual a: ", res)
                select = 0
            elif select == 5:
                x = float(input("Ingresa el numero en grados para optener su razon trigonometrica: "))
                res = 1/math.con(x)
                print("El resultado de la secante de ", x, " es igual a: ", res)
                select = 0
            elif select == 6:
                x = float(input("Ingresa el numero en grados para optener su razon trigonometrica: "))
                res = 1 / math.sin(x)
                print("El resultado de la cosecante de ", x, " es igual a: ", res)
                select = 0
            elif select == 7:
                calcul.bye(self=0)
                bandera1 = 2
            else:
                print("--------------------------------------------------")
                print("El numero seleccionado no existe, intente de nuevo")
                print("--------------------------------------------------")