import re
dicc={"azul":"blue","rojo":"red","verde":"green"}
bandera = 1
#bandera2 = 1
#trad = []

while bandera == 1:
    trad = []
    bandera2 = 1
    print("--------------------------")
    print("Diccionario ingles-español")
    print(" 1.Agregar palabras al diccionario")
    print(" 2.Imprimir diccionario")
    print(" 3.Traducir frase")
    print(" 4.Salir")
    print("--------------------------")
    select = int(input("Seleccione un numero: "))

    if select == 1:
        while bandera2 == 1:
            x = input("Ingrese la palabra que desea agregar: ")
            y = input("ingrese la palabra en ingles: ")
            for i in dicc:
                if i == x:
                    print("La palabra que deseas agregar ya existe en el diccionario")
                    break
                else:
                    dicc[x] = y
                    print(dicc)
                    bandera2 = 2
                    break
        select = 0
    elif select == 2:
        print(dicc)
        select = 0
    elif select == 3:
        frase = input("Ingrese la frase que deseas traducir: ")
        patron = r"\W+"
        palabras = re.split(patron, frase)
        for j in palabras:
            for i in dicc:
                if i == j:
                    trad.append(dicc[i])
                else:
                    continue
        print(*trad)
        select = 0
        #print(frase.replace(x,y))
    elif select == 4:
        print("-------------")
        print("vuelva pronto")
        print("-------------")
        bandera = 2

    else:
        print("El valor que eligio no existe vuelva a intentar")





