from multi import multi
from restar import res
from suma import sum
from division import div
from exponente import expo
from calculo import calcul
from funciones import function

bandera1 = 1
while bandera1 == 1:
    print("----------------------------------")
    print("Calculadora")
    print(" 1.Suma")
    print(" 2.Resta")
    print(" 3.Multiplicación")
    print(" 4.Division")
    print(" 5.Exponenciales")
    print(" 6.Funciones Trigonometricas")
    print(" 7.Salir")
    print("-----------------------------------")
    select = int(input("Seleccione un numero: "))
    if select == 1:
        sum.ans(self=0)
        select = 0
    elif select == 2:
        res.ans(self=0)
        select = 0
    elif select == 3:
        multi.ans(self=0)
        select = 0
    elif select == 4:
        div.ans(self=0)
        select = 0
    elif select == 5:
        expo.ans(self=0)
        select = 0
    elif select == 6:
        function.ans(self=0)
        select = 0
    elif select == 7:
        calcul.bye(self=0)
        bandera1 = 2
    else:
        print("--------------------------------------------------")
        print("El numero seleccionado no existe, intente de nuevo")
        print("--------------------------------------------------")






